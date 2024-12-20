"""
Django settings for hospitals_api project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import environ
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

env=environ.Env(DEBUG=(bool,False))

env = environ.Env(DEBUG=(bool, False))

environ.Env.read_env(env_file=".env")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")

ALLOWED_HOSTS = env("ALLOWED_HOSTS").split(" ")

# If the paths are inside the virtual environment folder, adjust this accordingly
# VENV_DIR = os.path.join(BASE_DIR, 'hospitalsenv', 'Lib', 'site-packages', 'osgeo')

# Set the relative paths
# PROJ_LIB = os.path.join(VENV_DIR, 'data', 'proj', 'proj.db')
# os.environ['GDAL_DATA'] = os.path.join(VENV_DIR, 'data', 'gdal')
# os.environ['PROJ_LIB'] = os.path.join(VENV_DIR, 'data', 'proj')
# os.environ['PATH'] = VENV_DIR + ";" + os.environ['PATH']

# Set GDAL_LIBRARY_PATH
# GDAL_LIBRARY_PATH = os.path.join(VENV_DIR, 'gdal.dll')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'i8t&7h4&dkcbho)qtko4l+#kv$8*2crexwmk0dz-9wz0^%_x!r'

# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# ALLOWED_HOSTS = []


# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'hospitals',
    'boundaries'
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'rest_framework_gis',
]

PROJECT_APPS = []

INSTALLED_APPS = DJANGO_APPS+THIRD_PARTY_APPS+PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hospitals_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'hospitals_api.wsgi.application'


# Database 
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": env("POSTGRES_DBNAME"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASS"),
        "HOST": env("PG_HOST"),
        "PORT": env("PG_PORT"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
