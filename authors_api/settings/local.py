from .base import *
from .base import env

DEBUG = True
# SECRET_KEY = 'django-insecure-ll#c60o!pna9efps58gd80#u)yc_1!=c&61r0#)c65h(^u&cmf'

SECRET_KEY = env(
    "DJANGO_SECRET_KEY", 
    default='django-insecure-ll#c60o!pna9efps58gd80#u)yc_1!=c&61r0#)c65h(^u&cmf'
)

ALLOWED_HOSTS = [
    'localhost',
    '0.0.0.0',
    '127.0.0.1'
]
