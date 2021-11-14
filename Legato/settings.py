"""
Django settings for Legato project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os.path
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-k5ioorwvgmh!_+y=5=s)ws)r7@h_ik5twx%$ep(u9d-6f#=!4#'

# SECURITY WARNING: don't run with debug turned on in production
DEBUG =True


#ALLOWED_HOSTS = ['vast-springs-24355.herokuapp.com']
#ALLOWED_HOSTS = ['afternoon-sea-44757.herokuapp.com']
#ALLOWED_HOSTS =['desolate-ocean-33028.herokuapp.com']
# Application definition
#ALLOWED_HOSTS=['nsoft-sample.herokuapp.com']

ALLOWED_HOSTS =['nsoft-sample.herokuapp.com','desolate-ocean-33028.herokuapp.com','127.0.0.1','upputurinagababu.herokuapp.com','upputurinagababu.herokuapp.com']
INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Profile',
    'widget_tweaks',
]
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'
ROOT_URLCONF = 'Legato.urls'

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

WSGI_APPLICATION = 'Legato.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
#
# DATABASES={
# 'default':{
#        'ENGINE':'djongo',
#        'NAME':'naga',
#         'CLIENT':{
#               'host':'mongodb+srv://naga:naga@naga.ky6ai.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
# }
# }
# }
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }




DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'naga-db',
        'USER': 'Naga',
        'PASSWORD': 'Jeevan$@123456',
        'HOST': 'ml-django.database.windows.net',
        'PORT': '1433',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
            'MARS_Connection': 'True',
        }
    }
}




# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'd4ed7psc5db8tr',
#         'HOST':'ec2-18-204-101-137.compute-1.amazonaws.com',
#         'USER':'vcczvtygmqsknh',
#         'PASSWORD':'6a107b6d5b992d8e663fcefea4ceea894b862ff1c1f096ed30565e3187f205c3',
#         'PORT':'5432',
#     }
# }



# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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




# EMAIL_HOST = 'smtp.google.com'
# EMAIL_HOST_USER = 'nagababuupputuri@gmail.com'
# EMAIL_HOST_PASSWORD = ''
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# STATIC_URL = '/static/'
# STATICFILES_DIRS=[
#      os.path.join(BASE_DIR,'static')
# ]
#
#
# MEDIA_URL='/media/'
# MEDIAFILES_ROOT=BASE_DIR

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = BASE_DIR
MEDIA_URL = '/media/'
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-secondary',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}
from  .email_info import *
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
