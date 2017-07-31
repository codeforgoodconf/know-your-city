"""
Django settings for Know Your City project.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/

For production hardening, see
https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/
"""
from pathlib import Path

from configurations import Configuration, values
from django.core.urlresolvers import reverse_lazy


class DjangoOverrides(Configuration):
    BASE_DIR = Path(__file__).parents[1]

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = values.SecretValue()

    # Set the login Redirect URL
    LOGIN_URL = reverse_lazy('login')
    LOGIN_REDIRECT_URL = reverse_lazy('index')

    SESSION_COOKIE_AGE = values.IntegerValue(1800)
    SESSION_EXPIRE_AT_BROWSER_CLOSE = values.BooleanValue(False)

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = values.BooleanValue(False)

    ALLOWED_HOSTS = []

    # Application definition
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.admindocs',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.humanize',
        'django.contrib.messages',
        'django.contrib.postgres',
        'django.contrib.sessions',
        'django.contrib.staticfiles',

        'kyc',
    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_URLCONF = 'kyc.urls'

    WSGI_APPLICATION = 'kyc.wsgi.application'

    # Database
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'HOST': 'db',
            'USER': values.Value(
                'postgres', environ_prefix='POSTGRES', environ_name='USER',
            ),
            'PASSWORD': values.SecretValue(
                environ_prefix='POSTGRES', environ_name='PASSWORD',
            ),
            'NAME': values.SecretValue(
                environ_prefix='POSTGRES', environ_name='DB',
            ),
        }
    }

    # Internationalization
    # https://docs.djangoproject.com/en/1.11/topics/i18n/
    LANGUAGE_CODE = 'en-us'
    TIME_ZONE = 'US/Eastern'
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True

    # Static asset configuration
    MEDIA_ROOT = '/public/media'
    MEDIA_URL = values.Value('/media/')
    STATIC_ROOT = '/public/static'
    STATIC_URL = values.Value('/static/')

    TEMPLATES = [{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': values.BooleanValue(DEBUG, environ_name='TEMPLATE_DEBUG'),
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.request',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    }]

    PASSWORD_HASHERS = [
        'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
        'django.contrib.auth.hashers.BCryptPasswordHasher',
        'django.contrib.auth.hashers.PBKDF2PasswordHasher',
        'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
        'django.contrib.auth.hashers.SHA1PasswordHasher',
        'django.contrib.auth.hashers.MD5PasswordHasher',
        'django.contrib.auth.hashers.CryptPasswordHasher',
    ]

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler'
            },
        },
        'loggers': {
            'ecogold': {
                'handlers': ['console'],
                'level': values.Value('INFO', environ_name='LOG_LEVEL'),
            },
        },
    }
