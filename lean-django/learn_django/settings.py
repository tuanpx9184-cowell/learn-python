"""
Django settings for learn_django project.

Generated by 'django-admin startproject' using Django 3.0.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f33p8=ir&0n1ud!3dhw8%q#$8ma(8p)eqazeq=sgc712w4ltdh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

IS_PRODUCTION = os.environ.get('DJANGO_SETTINGS_MODULE', '') == 'envs.production'
IS_STAGING = os.environ.get('DJANGO_SETTINGS_MODULE', '') == 'envs.staging'
IS_TESTING = os.environ.get('DJANGO_SETTINGS_MODULE', '') == 'envs.testing'

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
]

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'learn_django.urls'

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

WSGI_APPLICATION = 'learn_django.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'


def __get_log_level():
    if IS_TESTING:
        return 'ERROR'
    if IS_PRODUCTION:
        return 'INFO'
    else:
        return 'DEBUG'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s: %(name)s:%(lineno)d %(process)d %(thread)d [%(levelname)s] - %(message)s',
            '()': 'djangocolors_formatter.DjangoColorsFormatter'
        },
        'simple': {
            'format': '{levelname} {asctime} {message}',
            'style': '{',
        }

    },
    'handlers': {
        'console': {
            'level': __get_log_level(),
            'filters': [],
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'sqllog': {
            'level': 'DEBUG',
            'filters': [],
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/sql.log'),
            'when': 'D',
            'interval': 1,
            'backupCount': 100,
            'formatter': 'verbose',
        },
        'info_file': {
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/infor.log'),
            'formatter': 'simple',
        },
    },
    'loggers': {
        # Djangoが出すログはERRORレベル以降を補足
        'django': {
            'handlers': ['console', 'info_file'],
            'level': 'INFO',
            'propagate': True,
        },

        # ormのログを出す
        'django.db.backends': {
            'handlers': ['sqllog', ],
            'level': 'DEBUG',
            'propagate': False,
        },
    }
}