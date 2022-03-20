from .base import *

DEBUG = True

INSTALLED_APPS += [
    'apps.products',
    'apps.companies',
    'rest_framework',
    'django_extensions',
    'mptt'
]

# REST FRAMEWORK
DFC = 'rest_framework.pagination.PageNumberPagination'
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': DFC,
    'PAGE_SIZE': 10
}
