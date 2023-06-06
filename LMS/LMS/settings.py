"""
Django settings for LMS project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path
from .jazzmin import JAZZMIN_SETTINGS

BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$q-5r0mxb%y(5k&l%1+c*@dc89_a7&pn)f=!wgm3d_mz!5-0%)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '10.2.6.144', '127.0.0.1', '*']

# Application definition

INSTALLED_APPS = [
    # 'admin_argon.apps.AdminArgonConfig',
    'jazzmin',
    'ckeditor',
    'crispy_forms',
    'widget_tweaks',
    'app',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',

]

CRISPY_TEMPLATE_PACK = 'bootstrap4'
# model fix in admin template
X_FRAME_OPTIONS = 'SAMEORIGIN'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'LMS.urls'
# Templates Directory
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

WSGI_APPLICATION = 'LMS.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
DATABASES = 3


if DEBUG and (DATABASES == 1):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'djangodemo',
            'USER': 'root',
            'PASSWORD': '',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
# if DEBUG and (DATABASES == 1):
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.mysql',
#             'NAME': 'django_course',
#             'USER': 'root',
#             'PASSWORD': '111111',
#             'HOST': '10.1.3.10',
#             'PORT': '3306',
#         }
#     }
elif DEBUG and (DATABASES == 2):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
elif DEBUG and (DATABASES == 3):
    DATABASES = {
        "default": {
            "ENGINE": "mssql",
            "NAME": "DJANGO_COURSE",
            "USER": "sa",
            "PASSWORD": "tranquan98.kt",
            "HOST": "10.2.6.73",
            "PORT": "1433",

        },
    }
elif (DATABASES == 4):
    DATABASES = {
        'default': {
            'ENGINE': 'sql_server.pyodbc',
            'NAME': 'DJANGO_COURSE',
            'USER': 'sa',
            'PASSWORD': 'tranquan98.kt',
            'HOST': '10.2.6.73',
            'PORT': '1433',

            'OPTIONS': {
                'driver': 'ODBC Driver 13 for SQL Server',
            },
        },
    }

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Bangkok'

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR, 'Media')
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = 'home'
# LOGOUT_REDIRECT_URL = 'login'

# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'thomasvu2000@gmail.com'
# EMAIL_HOST_PASSWORD = 'bpgogoyrkizmiacj'


EMAIL_HOST = 'smtp.ansv.vn'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'vutuhoc@ansv.vn'
EMAIL_HOST_PASSWORD = 'Hoc@123'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

KEY_ID = ''
KEY_SECRET = ''

# CONFIG JET
JAZZMIN_SETTINGS = JAZZMIN_SETTINGS
JAZZMIN_SETTINGS["show_ui_builder"] = True
JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": True,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-orange",
    "sidebar_nav_small_text": True,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "default",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    },
    "actions_sticky_top": True
}
