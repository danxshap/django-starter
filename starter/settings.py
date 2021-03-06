import os
from os import environ

import dj_database_url
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS

DEBUG = True
TEMPLATE_DEBUG = DEBUG

PROJECT_PATH = os.path.abspath(os.path.join(__file__, os.path.pardir))

# Helper lambda for gracefully degrading environmental variables:
env = lambda e, d: environ[e] if environ.has_key(e) else d  

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

# Production
if env('I_AM_HEROKU', '') == '1':
    DEBUG = False
    TEMPLATE_DEBUG = DEBUG
    STATIC_URL = 'http://s3.amazonaws.com/django_starter/'
    ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
    TEMPLATE_DIRS = ('/app/starter/templates') 
    STATICFILES_STORAGE = 'custom_storages.S3PipelineStorage'
    AWS_STORAGE_BUCKET_NAME = 'django_starter'
    AWS_S3_SECURE_URLS = False
    AWS_QUERYSTRING_AUTH = False

    # Heroku database config
    DATABASES = {
        'default': dj_database_url.config()
    }

# Development
else:
    DEBUG = True
    TEMPLATE_DEBUG = DEBUG
    STATIC_URL = '/static/'
    ADMIN_MEDIA_PREFIX = '/static/admin/'
    TEMPLATE_DIRS = ('/sites/django-starter/starter/templates')
    STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

    # Local database config
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2', 
            'NAME': 'starter',
            'USER': 'postgres',
            'PASSWORD': '',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

# Auth stuff
LOGIN_URL = '/login'
LOGOUT_URL = '/logout'
LOGIN_REDIRECT_URL = '/'

# Email stuff
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True 
# SERVER_EMAIL = 'The Server <root@mysite.com>'
# EMAIL_HOST_USER = env('SITE_EMAIL_HOST_USER', '')
# EMAIL_HOST_PASSWORD = env('SITE_EMAIL_HOST_PASSWORD', '')

# Pipeline
BASE_CSS = ('main/bootstrap/css/bootstrap.css',
    'main/bootstrap/css/bootstrap-responsive.css','main/css/core.css',)
BASE_JS = ('main/js/csrf_setup.js', 'main/bootstrap/js/bootstrap.js',)

PIPELINE_CSS = {
    'standard': {
        'source_filenames': BASE_CSS,
        'output_filename': 'compressed_css/standard.min.css',
        'variant': 'datauri'
    }
}
PIPELINE_JS = {
    'standard': {
        'source_filenames': BASE_JS,
        'output_filename': 'compressed_js/standard.min.js',
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
# SECRET_KEY = '!0hg8t!*se&amp;r*_*&amp;^y=8!8)()5x*ztxqq#m4k8)g9liav#v-%1'
SECRET_KEY = env('DJANGO_SECRET_KEY', '')

# To make the {{ request }} template variable available for setting the login redirect URL to the current page (i.e. /login/?next={{ request.get_full_path }} )
TEMPLATE_CONTEXT_PROCESSORS = TEMPLATE_CONTEXT_PROCESSORS + ('django.core.context_processors.request', ) 

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'south',
    'storages',
    'pipeline',
    'apps.main'
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
