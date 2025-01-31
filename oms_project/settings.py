import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
MEDIA_DIR = os.path.join(BASE_DIR, 'media')



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-64++8ey#nh1#-fv=_i#$jcu*5$1qg$wad^w8c83cndy$gyfi^u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #  paypal
   #  'paypal.standard.ipn',
    # App Install
    'accounts',
    'Ambulance',
    'Hospital',
    'Doctors',
    'appointments',
    'medicine_store',
    'cart',
    'payments',

    #'blogs',
    #'donors',
    #'ambulances',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'oms_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR,],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'oms_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'oms',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = [
    'accounts.backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',  # Keep the default as a fallback
]

AUTH_USER_MODEL = 'accounts.User'
LOGIN_URL = '/user/login/'

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    STATIC_DIR,
]
MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = '/media/'


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#My added
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
# Timeout session after 30 minutes of inactivity
SESSION_COOKIE_AGE = 1800  
SESSION_SAVE_EVERY_REQUEST = True


DEBUG = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # Use SMTP backend
EMAIL_HOST = 'smtp.gmail.com'  # Gmail's SMTP server
EMAIL_PORT = 587  # Port for TLS
EMAIL_USE_TLS = True  # Enable TLS
EMAIL_HOST_USER = 'ashaduzzaman099@gmail.com'  # Replace with your Gmail address
EMAIL_HOST_PASSWORD = 'mvhfqbtcxyyrcvgv'  # Replace with your Gmail app password
DEFAULT_FROM_EMAIL = 'ashaduzzaman099@gmail.com'  # Default "from" address



PAYPAL_CLIENT_ID = 'Ac0Q-lwRvK3FoMrUhcSwoFeOQC01EkVUytq7A6MSMhHtlFqZJb7vYw_I33L5LSSkZoq7Q-hJKRXce1Cl'
PAYPAL_SECRET = 'Ac0Q-lwRvK3FoMrUhcSwoFeOQC01EkVUytq7A6MSMhHtlFqZJb7vYw_I33L5LSSkZoq7Q-hJKRXce1Cl'
PAYPAL_ENVIRONMENT = 'sandbox' 

