"""
Django settings for aconfig project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)

if not DEBUG:
    ALLOWED_HOSTS = ['.bafrocodes.co.tz', 'bafrocodes.co.tz', 'www.bafrocodes.co.tz']
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SESSION_COOKIE_SECURE = True
    SESSION_EXPIRE_AT_BROWSER_CLOSE = True
else:
    ALLOWED_HOST = []
    GOOGLE_RECAPTCHA_SECRET_KEY = config('GOOGLE_RECAPTCHA_SECRET_KEY')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
        #My_Apps
    'main',
    
        #Others
    'widget_tweaks',
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

ROOT_URLCONF = 'aconfig.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'aconfig.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

if not DEBUG:
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.mysql',
			'NAME': config('DB_NAME'),
			'USER': config('DB_USER'),
			'PASSWORD': config('DB_PASSWORD'),
			'HOST': config('DB_HOST'),
			'PORT': config('DB_PORT', cast=int),
			'OPTIONS': {
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
            },
		}
	}

else:
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.sqlite3',
			'NAME': str(BASE_DIR / 'db.sqlite3'),
		}
	}



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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Dar_es_Salaam'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATICFILES_DIRS = [BASE_DIR / 'static']

if not DEBUG:
	STATIC_ROOT = '/home/edukeaco/public_html/static/'
	MEDIA_URL = '/media/'
	MEDIA_ROOT = [BASE_DIR / 'media']
else:
	MEDIA_ROOT = 'media/'
	

if not DEBUG:
	BASE_URL = config('BASE_URL')
else:
	BASE_URL = 'http://127.0.0.1:8000'


if not DEBUG:
	EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
	EMAIL_HOST = config('EMAIL_HOST')
	EMAIL_HOST_USER = config('EMAIL_HOST_USER')
	EMAIL_PORT = config('EMAIL_PORT', cast=int)
	EMAIL_USE_SSL = config('EMAIL_USE_SSL', cast=bool)
	EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
	DEFAULT_FROM_EMAIL = 'noreply@edukea.co.tz'
	ADMIN_EMAIL = 'admin@edukea.co.tz'
else:
	DEFAULT_FROM_EMAIL = 'noreply@jaybla.com'
	EMAIL_HOST_USER = 'noreply@jaybla.com'
	EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
	EMAIL_FILE_PATH = str(BASE_DIR / 'sent_mails')
	ADMIN_EMAIL = 'admin@jaybla.com'


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
