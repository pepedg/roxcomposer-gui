# encoding: utf-8
#
# Global Django settings.
#
# devs@droxit.de
#
# Copyright (c) 2019 droxIT GmbH
#

"""
Django settings for roxgui project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import configparser
import logging
import os

import requests

logger = logging.getLogger(__name__)

# Base directory.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Read user specific settings from config.ini file.
config = configparser.ConfigParser()
config.read("config.ini")

# Initialize default service directory.
SERVICE_DIR = os.path.join(BASE_DIR, "services")
# Update service directory as specified in config file.
tmp_service_dir = config.get("Default", "ServiceDir", fallback=None)
if tmp_service_dir is not None:
    # Custom service directory is specified.
    if os.path.isdir(tmp_service_dir):
        # Custom service directory is valid and can be used.
        SERVICE_DIR = tmp_service_dir
    else:
        # Exit with error: Custom service directory is invalid.
        logger.error("Service directory specified in config file is invalid.")
        exit(1)

# Initialize default session directory.
SESSION_DIR = os.path.join(BASE_DIR, "sessions")
# Update session directory as specified in config file.
tmp_session_dir = config.get("Default", "SessionDir", fallback=None)
if tmp_session_dir is not None:
    # Custom session directory is specified.
    if os.path.isdir(tmp_session_dir):
        # Custom session directory is valid and can be used.
        SESSION_DIR = tmp_session_dir
    else:
        # Exit with error: Custom service directory is invalid.
        logger.error("Session directory specified in config file is invalid.")
        exit(1)

# Initialize path to ROXcomposer log file.
tmp_log_file = config.get("Default", "RoxComposerLogFile", fallback=None)
if tmp_log_file is not None:
    # ROXComposer log file is specified.
    if os.path.isfile(tmp_log_file):
        # Log file is valid and can be used.
        ROX_COMPOSER_LOG_FILE = tmp_log_file
    else:
        # Exit with error: Log file is invalid.
        logger.error("Path to ROXcomposer log file is invalid.")
        exit(1)

# Initialize ROXconnector connection data as specified in config file.
tmp_ip = config.get("Default", "RoxConnectorIp", fallback=None)
if tmp_ip is not None:
    # ROXconnector connection data is specified.format(service_name))
    ROX_CONNECTOR_IP = tmp_ip
    # Check if ROXconnector is actually running.
    try:
        requests.get("http://{}".format(tmp_ip))
    except requests.exceptions.ConnectionError:
        # Exit with error: ROXconnector is not running.
        logger.error("ROXconnector is not running.")
        exit(1)
else:
    # Exit with error: ROXconnector connection data is not specified.
    logger.error("ROXconnector connection data specified in config file is invalid.")
    exit(1)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=@f8-_+&ofu4=t1r)@3l!g7nko6g3ln3@8c3h*3(oyo7=yohc+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    # Custom apps.
    'web.apps.WebConfig',

    # Default apps.
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    # Default middleware.
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'roxgui.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Search for each app's template files in
        # corresponding local "templates" folder.
        'DIRS': [
            os.path.join(BASE_DIR, "templates"),
        ],
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

WSGI_APPLICATION = 'roxgui.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'de-de'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

# Location of global static files.
STATIC_URL = '/static/'

# Search for each app's static files
# in corresponding local "static" folder.
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# Directory in which all files from static folders will be copied.
STATIC_ROOT = os.path.join(BASE_DIR, "static_root")
