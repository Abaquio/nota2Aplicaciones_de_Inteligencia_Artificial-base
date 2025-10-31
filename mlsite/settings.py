"""
Django settings for mlsite project.

Generado por 'django-admin startproject' con Django 5.1.x
"""

from pathlib import Path
import os

# --- Paths ---
BASE_DIR = Path(__file__).resolve().parent.parent

# --- Seguridad ---
# (usa la que ya tenías; la mantengo para no romper el proyecto)
SECRET_KEY = 'django-insecure-%^cw5r8be*$0=x0w^%u0i!8l6@p5pd7ofb8%osu_tjswts%t@_'

# En producción debe ir False (en Render ya lo usas en False)
DEBUG = False

# Permite tu dominio de Render (o todos, para entrega académica)
ALLOWED_HOSTS = ["*"]
# Si quieres especificar, reemplaza por tu dominio:
# ALLOWED_HOSTS = ["nota2aplicaciones-de-inteligencia.onrender.com", "localhost", "127.0.0.1"]

# --- Aplicaciones ---
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # agrega aquí tus apps si las tienes (por ejemplo "diabetes", "insurance")
]

# --- Middleware ---
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # WhiteNoise para servir estáticos en producción
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "mlsite.urls"

# --- Templates ---
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # opcional si usas carpeta templates/
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "mlsite.wsgi.application"

# --- Base de datos ---
# Para la entrega usa SQLite (no requiere librerías nativas)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# --- Password validation ---
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# --- Internacionalización ---
LANGUAGE_CODE = "es-cl"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# --- Archivos estáticos (CSS, JS, imágenes) ---
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"        # para collectstatic en Render
STATICFILES_DIRS = [BASE_DIR / "static"] if (BASE_DIR / "static").exists() else []

# WhiteNoise: comprime y versiona archivos estáticos
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# --- Archivos multimedia (si los usas; si no, puedes omitir) ---
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# --- Clave primaria por defecto ---
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"