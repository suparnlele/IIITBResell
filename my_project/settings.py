"""
Django settings for my_project project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v+iec#4ktlk80pe5ck=i_#0c3il9267(&km6wxl@6i9^4j9_2!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition


LOGGING = {
  'version': 1,
  'disable_existing_loggers': False,
  'formatters': {
      'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'standard': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s %(filename)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
  },
  'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'file': {
            'level':'INFO',
            'class':'logging.FileHandler',
            'filename': BASE_DIR + "/logfile",
            #'maxBytes': 50000,
            #'backupCount': 2,
            'formatter': 'standard',
        },
        #'logstash': {
        #    'level': 'INFO',
        #    'class': 'logstash.TCPLogstashHandler',
        #    'host': '127.0.0.1',
        #    'port': 5959, #Default value: 5959
        #    'version': 1, # Version of logstash event schema. Default value: 0 (for backward compatibility of the library)
        #    'message_type': 'django_logstash',  # 'type' field in logstash message. Default value: 'logstash'.
        #    'fqdn': False, # Fully qualified domain name. Default value: false.
        #    'tags': ['django.request'], # list of tags. Default: None.
        #},
  },
  'loggers': {
        #'django.request': {
        #    'handlers': ['logstash'],
        #    'level': 'INFO',
        #    'propagate': True,
        #},
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}









INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts.apps.AccountsConfig',
    'crispy_forms',
    'first_app',
    'bootstrap3',
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

ROOT_URLCONF = 'my_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'my_project.wsgi.application'


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]

MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'


LOGIN_REDIRECT_URL = 'product_list'
LOGOUT_REDIRECT_URL = 'home'

EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = os.path.join(BASE_DIR, "sent_emails")


AUTH_USER_MODEL = 'accounts.CustomUser' # new
