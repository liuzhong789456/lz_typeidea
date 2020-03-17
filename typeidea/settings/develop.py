# flake8: NOQA
from .base import *

DEBUG = True
DATABASES = {
    'default': {
         'ENGINE': 'django.db.backends.mysql',
         'NAME': 'typeidea',
         'USER': 'root',
         'PASSWORD': 'Tb5111705_88',
         'HOST': '129.211.25.38',
         'PORT': 3306
    }
}
