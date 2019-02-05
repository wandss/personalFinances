import datetime
from .base import *

SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = False

ALLOWED_HOSTS = ['*']

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA':datetime.timedelta(days=90),
    # 'JWT_VERIFY_EXPIRATION':False,
}

#STATIC_ROOT = os.path.join(BASE_DIR, 'statics')
STATIC_ROOT = root('statics')
