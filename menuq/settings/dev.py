from .base import *

DEBUG = True

INSTALLED_APPS += [
    'apps.products',
    'apps.companies',
    'rest_framework',
    'django_extensions',
    'mptt',
    'django_countries'
]

# REST FRAMEWORK
DFC = 'rest_framework.pagination.PageNumberPagination'
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': DFC,
    'PAGE_SIZE': 10
}

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'menuq-db',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
