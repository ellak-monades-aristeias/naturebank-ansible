from naturebank_project.settings.base import *


DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = ({% for admin in naturebank_admins %}
    ('{{ admin.name }}', '{{ admin.email }}'),
{% endfor %})
MANAGERS = ADMINS
EMAIL_BACKEND = "django_sendmail_backend.backends.EmailBackend"
EMAIL_SUBJECT_PREFIX = '[Naturebank] '
SERVER_EMAIL = '{{ naturebank_server_email }}]'

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'naturebank',
        'HOST': 'localhost',
        'USER': 'naturebank',
        'PASSWORD': '{{ naturebank_secret_key }}',
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'stderr': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        },
    },
    'loggers': {
        'django': {
            'level': 'ERROR',
            'propagate': True,
            'handlers': ['stderr', 'mail_admins'],
        },
    },
}

ALLOWED_HOSTS = ['{{ naturebank_server_name }}']

AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.RemoteUserBackend',)

TIME_ZONE = 'Europe/Athens'
LANGUAGE_CODE = 'en-us'

LANGUAGES = (
    ('en', 'English'),
    ('el', 'Greek')
)

DEFAULT_LANGUAGE = 1

SITE_ID = 1

# Static files
MEDIA_ROOT = '/var/local/naturebank'
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
STATIC_ROOT = '/usr/local/naturebank-staticfiles/'

SECRET_KEY = '{{ naturebank_secret_key }}'

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'custom_middleware.RemoteUserCustomHeaderMiddleware',
    'pagination.middleware.PaginationMiddleware',
    'django_sorting.middleware.SortingMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

SECURE_PROXY_SSL_HEADER = ('HTTP_X_SCHEME', 'https')
SESSION_COOKIE_SECURE = True

{% if naturebank_customization_name %}
TEMPLATE_DIRS = ['/usr/local/{{ naturebank_customization_name}}/templates']
STATICFILES_DIRS = ['/usr/local/{{ naturebank_customization_name}}/static']
{% endif %}
