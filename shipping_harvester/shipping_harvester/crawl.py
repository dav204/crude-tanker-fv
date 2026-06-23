"""Discovery. Turn an aggregator's category archive into a list of ReportRefs.

Both sites are WordPress, so we try the WP REST API first (clean JSON, stable)
and fall back to HTML scraping the category pagination if REST is unavailable.

The two genuinely site-specific things are:
  1. the category slug (in config), and
  2. how the 'Download PDF' link sits in the post body.
Everything else is generic WordPress.
"""
from __future__ import annotations

import datetime as dt
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from . import config
from .models import ReportRef
from .net import PoliteSession


# --- helpers ----------------------------------------------------------------
def _parse_date(s: str) -> dt.date:
    # WP gives ISO like '2026-06-03T07:00:00'
    return dt.datetime.fromisoformat(s.replace("Z", "+00:00")).date()


def _extract_pdf_url(html: str, base: str) -> str | None:
    """Find the issue PDF link inside post content.

    Strategy: prefer an <a> whose href ends in .pdf; otherwise an <a> whose
    visible text mentions 'download'. Returns an absolute URL or None.
    """
    soup = BeautifulSoup(html, "lxml")
    # 1) explicit .pdf hrefs
    for a in soup.find_all("a", href=True):
        if a["href"].lower().split("?")[0].endswith(".pdf"):
            return urljoin(base, a["href"])
    # 2) "Download PDF" style links
    for a in soup.find_all("a", href=True):
        if "download" in a.get_text(strip=True).lower():
            return urljoin(base, a["href"])
    return None


# --- WordPress REST path ----------------------------------------------------
def _wp_category_id(session: PoliteSession, base: str, slug: str) -> int | None:
    url = f"{base}/wp-json/wp/v2/categories?slug={slug}"
    try:
        resp = session.get(url, expect="json")
        data = resp.json()
        return data[0]["id"] if data else None
    except Exception:
        return None


def _crawl_wp_rest(
    session: PoliteSession, base: str, source_id: str, cat_id: int, max_pages: int
) -> list[ReportRef]:
    refs: list[ReportRef] = []
    for page in range(1, max_pages + 1):
        url = (
            f"{base}/wp-json/wp/v2/posts?categories={cat_id}"
            f"&per_page=100&page={page}"
            f"&_fields=link,title,date_gmt,content"
        )
        try:
            resp = session.get(url, expect="json")
        except Exception:
            break
        posts = resp.json()
        if not posts:
            break
        for p in posts:
            title = BeautifulSoup(p["title"]["rendered"], "lxml").get_text(strip=True)
            broker = config.identify_broker(title)
            if broker is None:
                continue
            pdf = _extract_pdf_url(p.get("content", {}).get("rendered", ""), base)
            refs.append(
                ReportRef(
                    broker_id=broker.broker_id,
                    source=source_id,
                    title=title,
                    post_url=p["link"],
                    pdf_url=pdf,
                    published=_parse_date(p["date_gmt"]),
                )
            )
        if len(posts) < 100:
            break
    return refs


# --- HTML fallback path -----------------------------------------------------
def _crawl_html(
    session: PoliteSession, base: str, source_id: str, category_path: str, max_pages: int
) -> list[ReportRef]:
    refs: list[ReportRef] = []
    for page in range(1, max_pages + 1):
        list_url = f"{base}{category_path}" if page == 1 else f"{base}{category_path}page/{page}/"
        try:
            resp = session.get(list_url)
        except Exception:
            break
        soup = BeautifulSoup(resp.text, "lxml")
        # WordPress themes vary; <article> with an entry-title link is the
        # common case. Adjust the selector if a site uses something exotic.
        articles = soup.select("article") or soup.select("div.post")
        if not articles:
            break
        found_this_page = 0
        for art in articles:
            a = art.select_one("h2 a, h3 a, .entry-title a, a[rel=bookmark]")
            if not a or not a.get("href"):
                continue
            title = a.get_text(strip=True)
            broker = config.identify_broker(title)
            if broker is None:
                continue
            time_el = art.select_one("time[datetime]")
            try:
                published = (
                    _parse_date(time_el["datetime"]) if time_el else dt.date.today()
                )
            except Exception:
                published = dt.date.today()
            # fetch the post to dig out the PDF link
            try:
                post_html = session.get(a["href"]).text
                pdf = _extract_pdf_url(post_html, base)
            except Exception:
                pdf = None
            refs.append(
                ReportRef(
                    broker_id=broker.broker_id,
                    source=source_id,
                    title=title,
                    post_url=a["href"],
                    pdf_url=pdf,
                    published=published,
                )
            )
            found_this_page += 1
        if found_this_page == 0:
            break
    return refs


# --- public entry points ----------------------------------------------------
def crawl_hsn(session: PoliteSession, max_pages: int = 40) -> list[ReportRef]:
    cat_id = _wp_category_id(session, config.HSN_BASE, config.HSN_CATEGORY_SLUG)
    if cat_id is not None:
        refs = _crawl_wp_rest(session, config.HSN_BASE, "hsn", cat_id, max_pages)
        if refs:
            return refs
    # fallback
    return _crawl_html(
        session, config.HSN_BASE, "hsn",
        f"/category/{config.HSN_CATEGORY_SLUG}/", max_pages,
    )


def crawl_capitallink(
    session: PoliteSession, slugs=config.CAPITALLINK_CONTRIBUTOR_SLUGS, max_pages: int = 20
) -> list[ReportRef]:
    refs: list[ReportRef] = []
    for slug in slugs:
        cat_id = _wp_category_id(session, config.CAPITALLINK_BASE, slug)
        if cat_id is not None:
            refs += _crawl_wp_rest(session, config.CAPITALLINK_BASE, "capitallink", cat_id, max_pages)
        else:
            refs += _crawl_html(
                session, config.CAPITALLINK_BASE, "capitallink",
                f"/category/contributors/{slug}/", max_pages,
            )
    return refs


def crawl_all(session: PoliteSession, **kw) -> list[ReportRef]:
    return crawl_hsn(session, **kw) + crawl_capitallink(session)
