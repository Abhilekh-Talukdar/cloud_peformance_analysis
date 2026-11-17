"""Environment-backed configuration helpers for the Django project."""

import os
from collections.abc import Mapping
from pathlib import Path

_TRUE_VALUES = frozenset({"1", "true", "yes", "on"})
_FALSE_VALUES = frozenset({"0", "false", "no", "off"})


def _environment(environ: Mapping[str, str] | None = None) -> Mapping[str, str]:
    return os.environ if environ is None else environ


def get_secret_key(environ: Mapping[str, str] | None = None) -> str:
    """Return the required Django secret key without surrounding whitespace."""
    secret_key = _environment(environ).get("DJANGO_SECRET_KEY", "").strip()
    if not secret_key:
        raise RuntimeError(
            "DJANGO_SECRET_KEY must be set to a non-empty, randomly generated value."
        )
    return secret_key


def get_bool_setting(
    name: str,
    default: bool,
    environ: Mapping[str, str] | None = None,
) -> bool:
    """Parse a boolean environment variable and reject ambiguous values."""
    raw_value = _environment(environ).get(name)
    if raw_value is None:
        return default

    normalized = raw_value.strip().lower()
    if normalized in _TRUE_VALUES:
        return True
    if normalized in _FALSE_VALUES:
        return False

    accepted = ", ".join(sorted(_TRUE_VALUES | _FALSE_VALUES))
    raise ValueError(f"{name} must be one of: {accepted}.")


def get_allowed_hosts(environ: Mapping[str, str] | None = None) -> list[str]:
    """Return configured hosts, defaulting to loopback and rejecting '*'. """
    raw_hosts = _environment(environ).get("DJANGO_ALLOWED_HOSTS")
    if raw_hosts is None:
        return ["localhost", "127.0.0.1"]

    hosts = [host.strip() for host in raw_hosts.split(",") if host.strip()]
    if not hosts:
        raise ValueError("DJANGO_ALLOWED_HOSTS must contain at least one hostname.")
    if "*" in hosts:
        raise ValueError("DJANGO_ALLOWED_HOSTS must not contain the wildcard '*'.")
    return hosts


def get_sqlite_database_path(
    base_dir: str | Path,
    environ: Mapping[str, str] | None = None,
) -> str:
    """Resolve an optional SQLite path relative to the project directory."""
    configured_path = _environment(environ).get("DJANGO_SQLITE_PATH", "").strip()
    if not configured_path:
        return str(Path(base_dir) / "db.sqlite3")

    path = Path(configured_path)
    if not path.is_absolute():
        path = Path(base_dir) / path
    return str(path)
