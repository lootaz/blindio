from .settings import *

print("[DEVELOPMENT SETTINGS]")

DEBUG = True
AUTH_PASSWORD_VALIDATORS = []

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blindio',
        'USER': 'postgres',
        'PASSWORD': 'toor',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}
