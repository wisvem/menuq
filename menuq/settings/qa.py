from .base import *
import os

DEBUG = False

INSTALLED_APPS += [
    'apps.menus',
    'apps.companies',
    'apps.base',
    'rest_framework',
    'django_extensions',
    'django_countries',
    'widget_tweaks'
]


# REST FRAMEWORK
DFC = 'rest_framework.pagination.PageNumberPagination'
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': DFC,
    'PAGE_SIZE': 10,
    # 'DEFAULT_FILTER_BACKENDS': [
    #     'django_filters.rest_framework.DjangoFilterBackend'
    # ]
}

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {                                                                                                                               
#     'default': {                                                                                                                            
#     'ENGINE': 'django.db.backends.sqlite3',                                                                                                 
#     'NAME': BASE_DIR / 'db.sqlite3',                                                                                                        
#     }                                                                                                                                       
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'wisvem$menuqdbtest',
        'PASSWORD': 'alohomora1',
        'HOST': 'wisvem.mysql.pythonanywhere-services.com'
    }
}

STATICFILES_FINDERS = [
  # First add the two default Finders, since this will overwrite the default.
  'django.contrib.staticfiles.finders.FileSystemFinder',
  'django.contrib.staticfiles.finders.AppDirectoriesFinder'
]

#STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MIDDLEWARE += [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'crum.CurrentRequestUserMiddleware'
]

INTERNAL_IPS = [
    "127.0.0.1"
]

ALLOWED_HOSTS = [
  'localhost',
  '127.0.0.1',
  'wisvem.pythonanywhere.com',

]
