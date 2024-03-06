import os

SECRET_KEY = os.getenv('SECRET_KEY', 'NEW_SECRET_KEY')
DATABASES = {
    'default': {
        'ENGINE': os.getenv('ENGINE', 'django.db.backends.mysql'),
        'NAME': os.getenv('NAME', 'DATABASE_NAME'),
        'USER': os.getenv('USER', 'DATABASE_USER'),
        'PASSWORD': os.getenv('PASSWORD', 'DATABASE_PASSWORD'),
        'HOST': os.getenv('HOST', ''),
        'PORT': os.getenv('PORT', ''),
        'OPTIONS': {
             'charset': 'utf8mb4' 
            },
        'TEST': {
            'CHARSET': "utf8mb4",
            'COLLATION': "utf8mb4_unicode_ci",
        }
    }
}
ALLOWED_HOSTS = [ 'localhost', os.getenv('ALLOWED_HOSTS', 'DOMAIN_NAME')]
BASESITE_URL = os.getenv('BASESITE_URL', 'YOUR_MAIN_URL')
DEBUG = os.getenv('DEBUG', True)
EMAIL_BACKEND = os.getenv('EMAIL_BACKEND', 'django.core.mail.backends.filebased.EmailBackend')
EMAIL_FILE_PATH = '/tmp/'
EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp.email.org')
EMAIL_PORT = os.getenv('EMAIL_PORT', 587)
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', True)
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', 'admin@email.org')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', 'password')
SERVER_EMAIL = os.getenv('SERVER_EMAIL', 'admin@email.org')
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL', 'admin@email.org')
EMAIL_TIMEOUT = os.getenv('EMAIL_TIMEOUT', 5)