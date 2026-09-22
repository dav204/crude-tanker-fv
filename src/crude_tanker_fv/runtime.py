"""Atomic local receipts, process locks, and commits scoped to owned paths."""
import fcntl
import json
import os
import subprocess
import tempfile
from contextlib import contextmanager
from pathlib import Path


def atomic_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix=path.name + ".", dir=path.parent)
    try:
        with os.fdopen(fd, "w") as handle:
            json.dump(data, handle, indent=2, sort_keys=True, allow_nan=False)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


@contextmanager
def locked(path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a") as handle:
        fcntl.flock(handle, fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(handle, fcntl.LOCK_UN)


def commit_paths(root, paths, subject):
    if not paths:
        return None
    # --only excludes other staged paths. Refuse partially staged owned paths.
    for path in paths:
        staged = subprocess.run(["git", "diff", "--cached", "--quiet", "--", path], cwd=root).returncode
        unstaged = subprocess.run(["git", "diff", "--quiet", "--", path], cwd=root).returncode
        if staged and unstaged:
            raise ValueError("partially staged automation path: " + path)
    subprocess.run(["git", "add", "--", *paths], cwd=root, check=True)
    if subprocess.run(["git", "diff", "--cached", "--quiet", "--", *paths], cwd=root).returncode:
        subprocess.run(["git", "commit", "--only", "-qm", subject, "--", *paths], cwd=root, check=True)
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
