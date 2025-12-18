"""
Django settings for CoolSense project.
"""

from pathlib import Path
import os
from pymongo import MongoClient

BASE_DIR = Path(__file__).resolve().parent.parent


# ================================
# SECRET KEY
# ================================
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "insecure-dev-key")


# ================================
# DEBUG
# ================================
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0', '*']  # '*' apenas para desenvolvimento


# ================================
# APPS
# ================================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'core',
    'sensors',
]


# ================================
# MIDDLEWARE
# ================================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'CoolSense.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'CoolSense.wsgi.application'


# ================================
# DATABASES (apenas Postgres)
# ================================
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB", "mydb"),
        "USER": os.environ.get("POSTGRES_USER", "myuser"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "mypassword"),
        "HOST": os.environ.get("POSTGRES_HOST", "db_postgres"),
        "PORT": os.environ.get("POSTGRES_PORT", "5432"),
    }
}


# ================================
# MONGO (PyMongo)
# ================================
MONGO_URI = os.environ.get("MONGO_URI", "mongodb://mongo:27017/coolsense")

try:
    mongo_client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    mongo_db = mongo_client["coolsense"]
    # Testa a conexão
    mongo_client.server_info()
except Exception as e:
    print(f"Warning: Could not connect to MongoDB: {e}")
    print("MongoDB connection will be retried when needed.")
    mongo_client = None
    mongo_db = None


# ================================
# PASSWORDS
# ================================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# ================================
# I18N
# ================================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# ================================
# STATIC
# ================================
STATIC_URL = 'static/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ================================
# REST FRAMEWORK
# ================================
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',  # Permite acesso sem autenticação (apenas para desenvolvimento)
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',  # Para facilitar testes
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ],
}
