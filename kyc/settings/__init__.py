from configurations import values

from .django_overrides import DjangoOverrides


class Development(DjangoOverrides):
    ALLOWED_HOSTS = ['*']
    INSTALLED_APPS = DjangoOverrides.INSTALLED_APPS + [
        'debug_toolbar',
        'django_extensions',
    ]
    INTERNAL_IPS = ['192.168.254.1']
    MIDDLEWARE = [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ] + DjangoOverrides.MIDDLEWARE

    COMPRESS_CSS_FILTERS = ['compressor.filters.css_default.CssAbsoluteFilter']
    COMPRESS_JS_FILTERS = []
