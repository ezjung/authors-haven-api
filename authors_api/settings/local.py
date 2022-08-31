import os
from .base import *
# from .base import environ

DEBUG = str(os.environ.get('DEBUG')) == "1"
# SECRET_KEY = 'django-insecure-ll#c60o!pna9efps58gd80#u)yc_1!=c&61r0#)c65h(^u&cmf'

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

ALLOWED_HOSTS = [
    'localhost',
    '0.0.0.0',
    '127.0.0.1'
]
