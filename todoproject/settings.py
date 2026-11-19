import os
from pathlib import Path

import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# ---------- Production / Render ----------

# Static files
STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Security — read from environment, fall back to local defaults
SECRET_KEY = os.environ.get("SECRET_KEY", "django-insecure-local-development-key")
DEBUG = os.environ.get("DEBUG", "True") == "True"

# Database — use DATABASE_URL from Render, or local SQLite
DATABASES = {
    "default": dj_database_url.config(
        default=f"sqlite:///{os.path.join(BASE_DIR, 'db.sqlite3')}",
        conn_max_age=600,
    )
}