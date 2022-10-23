"""
Django settings for bp_app_web project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
import cloudinary_storage
import dj_database_url


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

#django-insecure-sz)%r2o-a1dz5cws3#j+q+lg+s67#^6#g&qf8z*)fep%7%309y

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', default='your secret key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
DEBUG = 'RENDER' not in os.environ ## si no existe devuelve True

ALLOWED_HOSTS = []
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'imagekit',
    'cloudinary_storage',
    'cloudinary',
    'AccessControl',
    'Material',
    'Asociado',
    'Actividades',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

]

ROOT_URLCONF = 'bp_app_web.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'bp_app_web/templates'],
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

WSGI_APPLICATION = 'bp_app_web.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
'''

'''
    DATABASES = {
        'default': {
            'ENGINE': 'mysql.connector.django',
            'NAME': 'a52hepof_bp324_mariadb',
            'USER': 'a52hepof_bp324_usuario',
            'PASSWORD': 'U74&a93iu',
            'HOST': 'tommy2.heliohost.org',
            'PORT': '',
        }
    }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'database324app',
        'USER': 'postgres324',
        'PASSWORD': 'U74&a93iu',
        'HOST': 'database-324-app.caqpfa3nnout.us-east-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}

'''
    


if DEBUG:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

     
else:
    DATABASES = {
        'default': dj_database_url.config(
            # Feel free to alter this value to suit your needs.
            #default='postgresql://postgres:postgres@localhost:5432/mysite',
            #conn_max_age=600
        )
}
print(DATABASES)

# PGPASSWORD=rJ447fT859pDdcUmVhtvTbqqa0QsiMMJ psql 
# -h dpg-cda0jl2en0hldb2fr98g-a.oregon-postgres.render.com 
# -U db_324app_user 
# db_324app


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

LOGIN_URL = 'signin'

LOGIN_REDIRECT_URL = '/admin/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR,"/static/")


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

if not DEBUG:    # Tell Django to copy statics to the `staticfiles` directory
    # in your application directory on Render.
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    # Turn on WhiteNoise storage backend that takes care of compressing static files
    # and creating unique names for each version so they can safely be cached forever.
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

APPEND_SLASH=False

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR,"/media/")

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
#DEFAULT_FILE_STORAGE = os.path.join(BASE_DIR,"/")

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'drewh18oi',
    'API_KEY': '781723622332121',
    'API_SECRET': 'TH2cumQaERQPKp_PZ6UAWvNfcAk',
    
}

#AUTH_USER_MODEL = 'accessAplication.usuarioPersonalizado'
CLOUDINARY_PATH = 'https://res.cloudinary.com/'+CLOUDINARY_STORAGE['CLOUD_NAME']+'/image/upload/v1/'
