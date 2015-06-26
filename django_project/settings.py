"""
Django settings for django_project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'Ur4RM1Q4MtU0FS0PbRdzJePxETqWr8fhNor7WuTcmfAnJnA1kl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']



# Application definition
#from south.db import db
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'glass',
    'tinymce',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'django_project.urls'

WSGI_APPLICATION = 'django_project.wsgi.application'

TINYMCE_DEFAULT_CONFIG = {
'theme': "advanced",
'skin': "o2k7",
'skin_variant': "silver",
'relative_urls': False,
'width': "640",
'height': "500",
'theme_advanced_toolbar_location': "top",
'theme_advanced_toolbar_align': "left",
'theme_advanced_statusbar_location': "bottom",
'theme_advanced_resizing': True,
'element_format': "html",
'plugins' :
"contextmenu,directionality,fullscreen,paste,preview,searchreplace,spellchecker,visualchars,wordcount,table",
'theme_advanced_buttons3_add' : "tablecontrols",
'table_styles' : "Header 1=header1;Header 2=header2;Header 3=header3",
'table_cell_styles' : "Header 1=header1;Header 2=header2;Header3=header3;Table Cell=tableCel1",
'table_row_styles' : "Header 1=header1;Header 2=header2;Header3=header3;Table Row=tableRow1",
'table_cell_limit' : 100,
'table_row_limit' : 5,
'table_col_limit' : 5,
'table_inline_editing': True,
}
# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'UBsQ7l3Vbl',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-sv'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_ROOT = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2]+['static'])
#STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'
STATIC_URL = '/static/'

#STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')


USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
