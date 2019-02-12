import datetime
from .base import *

SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = True

ALLOWED_HOSTS = ['*']

#CORS_ORIGIN_ALLOW_ALL = True

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=10),
    # 'JWT_VERIFY_EXPIRATION': False,
}
