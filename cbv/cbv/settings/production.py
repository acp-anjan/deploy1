import dj_database_url
from cbv.settings import *
import os


SECRET_KEY =  os.environ.get('SECRET_KEY')

DEBUG = False

DATABASES = {
    'default': dj_database_url.config()
}