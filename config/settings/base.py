"""
Django settings for ferah project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'r4g=k%!&nec0v@xt@9oi@e17h3%#7v3cgmg*p2_!cq2a&r*fp#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'south',
    'storages',

    'apps.conversations',
    'apps.home',
    'apps.login',
    'apps.tags',
    'apps.utils',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

LOGIN_URL = '/login/'

LOGIN_REDIRECT_URL = '/login/'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

if 'test' in sys.argv:
    DATABASES = {'default': {'ENGINE':'django.db.backends.sqlite3'}}
else:
    DATABASES = {
        'default': {
            'ENGINE':'django.db.backends.postgresql_psycopg2',
            'NAME': 'ferah',
            'USER': '',
            'PASSWORD': '',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/London'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Date
DATETIME_FORMAT = '%B %d, %Y, %I:%M, %p'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)