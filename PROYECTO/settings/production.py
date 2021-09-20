from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':'bdproyecto',
        'USER':'postgres',
        'PASSWORD':'1234',
        'HOST':'127.0.0.1',
        'DATABASE_PORT':'5432'
    }
}

