# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-fwic9g(9#(av(#$_--#!!s(p1m+qogtx@v=m7)lse=z*+x^m65'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'products_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Shamgar1'
    }
}