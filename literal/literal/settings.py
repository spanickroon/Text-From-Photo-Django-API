import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")


DEBUG = os.environ.get("DEBUG")


ALLOWED_HOSTS = ["127.0.0.1", "0.0.0.0", "localhost"]


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework.authtoken",
    "apps.authentication",
    "apps.mailer",
    "apps.scanner",
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


ROOT_URLCONF = "literal.urls"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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


WSGI_APPLICATION = "literal.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DATABASE_ENGINE"),
        "NAME": os.environ.get("PG_DB"),
        "USER": os.environ.get("PG_USER"),
        "PASSWORD": os.environ.get("PG_USER_PASSWORD"),
        "HOST": os.environ.get("PG_HOST"),
        "PORT": os.environ.get("PG_PORT"),
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.authentication.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.authentication.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.authentication.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.authentication.password_validation.NumericPasswordValidator",
    },
]


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ]
}


LANGUAGE_CODE = "en-us"

TIME_ZONE = "Europe/Minsk"

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = "/staticfiles/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
