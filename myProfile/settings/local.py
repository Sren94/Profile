
from .base import *
import os
import environ
import dj_database_url
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = env('SECRET_KEY')
DEBUG = env.bool('DEBUG', default=False)

#SECRET_KEY = 'django-insecure-lzhsaphvh5#fkds4tfjz(*eoy=mr(of&i%mi9x%u&p-d67jfe='

#DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL')
    )
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME':env('NAME_DATABASE'),
    #     'USER':env('DB_USER'),
    #     'PASSWORD':env('DB_PASSWORD'),
    #     'HOST':env('HOST'),
    #     'PORT':'5432',
    # }
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME':env('NAME_DATABASE'),
    #     'USER':env('DB_USER'),
    #     'PASSWORD':env('DB_PASSWORD'),
    #     'HOST':'localhost',
    #     'PORT':'5432',
    # }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
STATIC_URL = 'static/'
STATICFILES_DIRS=[os.path.join(BASE_DIR, "static")]

#aqui se da registro de los archivos media 
#y esto sirve para direccionar los recursos
#se deben de registrar en esta carpeta
MEDIA_URL='media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
# settings.py
# settings.py


# Configuraciones de email

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # O el servidor de correo que uses
EMAIL_PORT = 587
EMAIL_USE_TLS = True
#EMAIL_HOST_USER ='stroop94@gmail.com'
EMAIL_HOST_USER=env('EMAIL_HOST_USER')
#print(env('EMAIL_HOST_USER'))
#EMAIL_HOST_PASSWORD ='nsgk uewt qafk fntm'
EMAIL_HOST_PASSWORD =env('EMAIL_HOST_PASSWORD')
#print(EMAIL_HOST_PASSWORD)