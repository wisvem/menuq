from .base import *

DEBUG = True

INSTALLED_APPS += [
    'apps.products',
    'rest_framework',
    'django_extensions',
]

# REST FRAMEWORK
DFC = 'rest_framework.pagination.PageNumberPagination'
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': DFC,
    'PAGE_SIZE': 10
}
