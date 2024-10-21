from .base import *
import os
import environ
import dj_database_url
import cloudinary
import cloudinary_storage
# Cargar las variables de entorno
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Clave secreta y configuración de depuración
SECRET_KEY = env('SECRET_KEY')
DEBUG = env.bool('DEBUG', default=False)

# Hosts permitidos
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=["localhost", "sren94.up.railway.app"])
#ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=["localhost"])

# Orígenes de confianza para CSRF
CSRF_TRUSTED_ORIGINS = env.list('CSRF_TRUSTED_ORIGINS', default=[])

# Configuración de la base de datos
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL')
    )
}

# Configuración de Cloudinary
# CLOUDINARY_STORAGE = {
#     'CLOUD_NAME': env('CLOUD_NAME'),
#     'API_KEY': env('API_KEY'),
#     'API_SECRET': env('API_SECRET'),
#     'PREFIX': 'static/'
# }

cloudinary.config(
    cloud_name=env('CLOUD_NAME'),
    api_key=env('API_KEY'),
    api_secret=env('API_SECRET'),
    secure=True,
)
#configuracion actualizada 
#STATIC_URL = '/static/'
#MEDIA_URL = '/media/'
STATIC_URL = 'https://res.cloudinary.com/dj3octk7q/static/'
MEDIA_URL = 'https://res.cloudinary.com/dj3octk7q/media/'

#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Almacenamiento de archivos estáticos en Cloudinary
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'

# Almacenamiento específico para archivos multimedia en Cloudinary
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
# Almacenamiento específico para videos
VIDEO_FILE_STORAGE = 'cloudinary_storage.storage.VideoMediaCloudinaryStorage'

# Almacenamiento específico para archivos de texto
RAW_FILE_STORAGE = 'cloudinary_storage.storage.RawMediaCloudinaryStorage'

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

