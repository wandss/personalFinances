from .base import *

SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LANGUAGE_CODE = 'pt-br'

ALLOWED_HOSTS = ['127.0.0.1', '192.168.15.2']

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR,'static_files')
#INSTALLED_APPS += ('apps related to this settings environment')
