from .base import *
import os
import environ
import dj_database_url
import cloudinary
# Import the cloudinary.api for managing assets
import cloudinary.api
# Import the cloudinary.uploader for uploading assets
import cloudinary.uploader

# Cargar las variables de entorno
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Clave secreta y configuración de depuración
SECRET_KEY = env('SECRET_KEY')
DEBUG = env.bool('DEBUG', default=False)

# Hosts permitidos
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])

# Orígenes de confianza para CSRF
CSRF_TRUSTED_ORIGINS = env.list('CSRF_TRUSTED_ORIGINS', default=[])

# Configuración de la base de datos
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL')
    )
}

# Configuración de Cloudinary
cloudinary.config(
    cloud_name= env('CLOUD_NAME'),
    api_key= env('API_KEY'),
    api_secret=env('API_SECRET'),
    secure=True,
)

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'

# URLs y rutas para archivos estáticos y media
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

# Configuración de email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True 
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')

# Configuración adicional
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Seguridad para producción
SECURE_SSL_REDIRECT = env.bool('SECURE_SSL_REDIRECT', default=False)
SESSION_COOKIE_SECURE = env.bool('SESSION_COOKIE_SECURE', default=False)
CSRF_COOKIE_SECURE = env.bool('CSRF_COOKIE_SECURE', default=False)


# from .base import *
# import os
# import environ
# import dj_database_url
# env = environ.Env()
# environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# SECRET_KEY = env('SECRET_KEY')
# DEBUG = env.bool('DEBUG', default=False)

# #SECRET_KEY = 'django-insecure-lzhsaphvh5#fkds4tfjz(*eoy=mr(of&i%mi9x%u&p-d67jfe='

# #DEBUG = True

# ALLOWED_HOSTS = [env('ALLOWED_HOSTS')]
# #CSRF_TRUSTED_ORIGINS = [env('CSRF_TRUSTED_ORIGINS')]
# DATABASES = {
#     'default': dj_database_url.config(
#         default=os.getenv('DATABASE_URL')
#     )
#     # 'default': {
#     #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
#     #     'NAME':env('NAME_DATABASE'),
#     #     'USER':env('DB_USER'),
#     #     'PASSWORD':env('DB_PASSWORD'),
#     #     'HOST':env('HOST'),
#     #     'PORT':'5432',
#     # }
#     # 'default': {
#     #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
#     #     'NAME':env('NAME_DATABASE'),
#     #     'USER':env('DB_USER'),
#     #     'PASSWORD':env('DB_PASSWORD'),
#     #     'HOST':'localhost',
#     #     'PORT':'5432',
#     # }
# }

# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/5.0/howto/static-files/
# STATIC_URL = '/static/'
# #STATICFILES_DIRS=[os.path.join(BASE_DIR, "static")]

# #aqui se da registro de los archivos media 
# #y esto sirve para direccionar los recursos
# #se deben de registrar en esta carpeta
# MEDIA_URL='/media/'
# MEDIA_ROOT=os.path.join(BASE_DIR,'media')
# # Default primary key field type
# # https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
# # settings.py
# # settings.py


# # Configuraciones de email

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'  # O el servidor de correo que uses
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# #EMAIL_HOST_USER ='stroop94@gmail.com'
# EMAIL_HOST_USER=env('EMAIL_HOST_USER')
# #print(env('EMAIL_HOST_USER'))
# #EMAIL_HOST_PASSWORD ='nsgk uewt qafk fntm'
# EMAIL_HOST_PASSWORD =env('EMAIL_HOST_PASSWORD')
# #print(EMAIL_HOST_PASSWORD)


# CLOUDINARY_STORAGE = {
#     'CLOUD_NAME': env('CLOUD_NAME'),
#     'API_KEY': env('API_KEY'),
#     'API_SECRET': env('API_SECRET'),
# }
# DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
# STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'

