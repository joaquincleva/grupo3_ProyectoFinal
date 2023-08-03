from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# Configuración para base de datos sqlite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'grupoinformatorio@gmail.com'
EMAIL_HOST_PASSWORD = 'yykvqmqfnkjvwftq'
# # Configuracion de base de datos MySQL
# DATABASES = {
#     'default': {
#         'ENGINE':
#         'NAME':
#         'USER':
#         'PASSWORD':
#         'HOST':
#     }
# }