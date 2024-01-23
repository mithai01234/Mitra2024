"""
Django settings for Mitra project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-d428@iu6&#y1@)zrb=1r&d8kd@kq_w2=%%a(l+_o&m1rkck7as'

ALLOWED_HOSTS = ['139.84.144.65']


# Application definition

INSTALLED_APPS = [
    'jazzmin',
     'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mitraapp',
     'rest_framework',
    'rest_framework_api_key',
    'corsheaders',
    'registration',
    'videoupload',
    'userlist',
    'report',
'videolist',
    'statusapp',
    'relationship',
    'backendlogin',
    'ott',
    # 'chatapp'
   # 'django_crontab',
]
# CRONJOBS = [
#     ('*/2 * * * *', 'status_app.management.commands.clean_statuses'),
# ]
# settings.py
TIME_ZONE = 'Asia/Kolkata'


MIDDLEWARE = [
     # 'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',

]


ROOT_URLCONF = 'Mitra.urls'
CORS_ORIGIN_ALLOW_ALL = True
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',


            ],
        },
    },
]
STATIC_URL = 'static/'

WSGI_APPLICATION = 'Mitra.wsgi.application'




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

#DATABASES = {
 #   'default': {
       # 'ENGINE': 'django.db.backends.postgresql',
      #  'NAME': 'defaultdb',
     #   'USER': 'vultradmin',
    #    'PASSWORD': 'AVNS_vnByfO1rdsrUscdj8D-',
   #     'HOST': 'vultr-prod-bebe66a4-d17b-49d6-bb33-553c4690dd58-vultr-prod-38e2.vultrdb.com',
  #      'PORT': '16751',
 #   }
#}
AUTH_USER_MODEL = 'registration.CustomUser'


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]



LANGUAGE_CODE = 'en-us'
# settings.py
TIME_ZONE = 'Asia/Kolkata'


USE_I18N = True

USE_TZ = True




STATIC_URL = 'static/'



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

#DEBUG = True
#ALLOWED_HOSTS = []

DEBUG = True

ALLOWED_HOSTS = ['*']
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
#216 219 212 database 221
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'srutee@gmail.com'
EMAIL_HOST_PASSWORD = ''



#
# AWS_ACCESS_KEY_ID = 'T5SG87Y94IKFIZBMNGOE'
# AWS_SECRET_ACCESS_KEY = '2rKkzzIvLYjrS0AVltlhIdmJtJ1sskbVe6ysld38'
# AWS_STORAGE_BUCKET_NAME = 'mitra-bucket'
# AWS_S3_ENDPOINT_URL = 'https://blr1.vultrobjects.com'
#
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# AWS_ACCESS_KEY_ID = 'DO006WCUVZ39QR8WGU7D'
# AWS_SECRET_ACCESS_KEY = '9WX8lYo2dTul2NQKPDbM5+AC1455O2GT+l69RI9ex7g'
# AWS_STORAGE_BUCKET_NAME = 'mitra-bucket'  # Replace with your Vultr Object Storage bucket name
# AWS_S3_ENDPOINT_URL = 'https://mitra-bucket.blr1.digitaloceanspaces.com'  # Use your Vultr Object Storage endpoint
# AWS_DEFAULT_ACL = 'public-read'
# # Use the Vultr S3Boto3Storage backend
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#

# settings.py

# ...

# Add these lines at the end of the file
AWS_ACCESS_KEY_ID = 'DO006WCUVZ39QR8WGU7D'
AWS_SECRET_ACCESS_KEY = '9WX8lYo2dTul2NQKPDbM5+AC1455O2GT+l69RI9ex7g'
AWS_STORAGE_BUCKET_NAME = 'mitra-bucket'
AWS_S3_REGION_NAME = 'blr1'
AWS_S3_ENDPOINT_URL = 'https://mitra-bucket.blr1.digitaloceanspaces.com'
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.{AWS_S3_REGION_NAME}.cdn.digitaloceanspaces.com/mitra-bucket"
AWS_DEFAULT_ACL = 'public-read'
# Use the following if your Space is in the default NYC3 region
# AWS_S3_ENDPOINT_URL = 'https://nyc3.digitaloceanspaces.com'

# Set the default storage engine to use S3
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
