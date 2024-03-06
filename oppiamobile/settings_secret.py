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