"""
Django settings for basic_movie_db project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

import dj_database_url
import environ


root = environ.Path(__file__) - 2  # type: collections.Callable
env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(root('.env'))  # reading .env file

ROOT_PATH = root

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'basic_movie_db',
    'rest_framework',
    'rest_framework_swagger',
    'django_filters',
    'storages'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'basic_movie_db.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ]
        }

    }
]

WSGI_APPLICATION = 'basic_movie_db.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': root('db.sqlite3'),
    }
}

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

# AWS s3
if env('AWS_ACCESS_KEY', default=None):
    # general setup
    AWS_S3_REGION_NAME = 'eu-west-1'
    AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY')
    AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_KEY')
    AWS_STORAGE_BUCKET_NAME = env('AWS_BUCKET_NAME')

    AWS_S3_CALLING_FORMAT = 'boto.s3.connection.OrdinaryCallingFormat'

    # media
    MEDIAFILES_LOCATION = 'media'
    DEFAULT_FILE_STORAGE = 'basic_movie_db.storages.MediaStorage'

    # static
    STATICFILES_LOCATION = 'static'
    STATICFILES_STORAGE = 'basic_movie_db.storages.StaticStorage'
    STATIC_URL = 'https://{}.s3.amazonaws.com/static/'.format(
        AWS_STORAGE_BUCKET_NAME)

    # collectfast before staticfiles
    INSTALLED_APPS = list(INSTALLED_APPS)
    index_staticfiles = INSTALLED_APPS.index('django.contrib.staticfiles')
    INSTALLED_APPS.insert(index_staticfiles, 'collectfast')
    INSTALLED_APPS = tuple(INSTALLED_APPS)

    STATIC_ROOT = root('staticfiles')

    MEDIA_URL = 'https://{}.s3.amazonaws.com/media/'.format(
        AWS_STORAGE_BUCKET_NAME)
    MEDIA_ROOT = root('media')

else:
    # Static/Media
    MEDIA_ROOT = root('media')
    MEDIA_URL = '/media/'

    STATIC_ROOT = root('static')
    STATIC_URL = '/static/'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}



REST_FRAMEWORK = {
    'PAGE_SIZE': 10,
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'EXCEPTION_HANDLER': 'rest_framework.views.exception_handler'
}

DEBUG = True

SWAGGER_SETTINGS = {
    'USE_SESSION_AUTH': False,
    'DOC_EXPANSION': 'list',
    'APIS_SORTER': 'alpha',
    'SECURITY_DEFINITIONS': None,
}
