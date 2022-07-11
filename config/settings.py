import os

# import dj_database_url
# import django_heroku
# from dotenv import load_dotenv

# load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = str(os.getenv('DJANGO_SECRET_KEY'))
DEBUG = True

# Authentication handler for django/allauth
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'hrmsysytem.herokuapp.com','.ngrok.io']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.humanize',
    'django.contrib.sites',

    # installed apps
    'rest_framework',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'pwa',
    'user_visit',
    'cloudinary_storage',
    'crispy_forms',
    'django_summernote',
    'django_filters',
    'phonenumber_field',
    'django_daraja',
    'slick_reporting',
    'django_extensions',

    'accounts.apps.AccountsConfig',
    'rental_property',
    'core',
    'utils.apps.UtilsConfig',
    'complaints',
    'work_order',
    'reporting.apps.ReportingConfig',
]

SITE_ID = 1
AUTH_USER_MODEL = 'accounts.User'

CSRF_TRUSTED_ORIGINS = ['https://*.ngrok.io',]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'user_visit.middleware.UserVisitMiddleware',
]

STRIPE_PUBLISHABLE_KEY = str(os.getenv('STRIPE_PUBLISHABLE_KEY'))
STRIPE_SECRET_KEY = str(os.getenv('STRIPE_SECRET_KEY'))
    
#handle staticfiles
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'rental_property.context_processors.my_managed_buildings',
                'accounts.context_processors.get_notifications',
                'complaints.context_processors.get_contacts',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':  'rentio1',
        'USER':'postgres',
        'PASSWORD':'toor',
        'HOST':'localhost',
        'PORT':'5432'
    }
}

#DATABASES['default'] = dj_database_url.config('postgres://USER:PASSWORD@HOST:PORT/NAME',conn_max_age=600)


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

MPESA_ENVIRONMENT = 'sandbox'
MPESA_CONSUMER_KEY = 'ok1GPtTX03RBGvKa918FS0XeAFrdDdXG'
MPESA_CONSUMER_SECRET = 'nMosJos4CkUSHlkp'
MPESA_SHORTCODE = '174379'
MPESA_EXPRESS_SHORTCODE = '174379'
MPESA_SHORTCODE_TYPE = 'paybill'
MPESA_PASSKEY = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
MPESA_INITIATOR_USERNAME = 'testapi'
MPESA_INITIATOR_SECURITY_CREDENTIAL = 'Safaricom979!'

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_TZ = True

#sendgrig email settings for notifications
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'#'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'benngovi47@gmail.com'
EMAIL_HOST_PASSWORD = '074143ben'
# EMAIL_HOST_USER = 'apikey'
# EMAIL_HOST_PASSWORD ='074143ben' #os.environ.get('SENDGRID_EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = 'RENTIO <benngovi47@gmail.com>'

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
COLLECTSTATIC = 1

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CRISPY_TEMPLATE_PACK = 'bootstrap4'

#cloudinary storage : handling imaeges in deployment

if DEBUG == False:
    CLOUDINARY_STORAGE = {
        'CLOUD_NAME': 'hqrwhofew',
        'API_KEY': os.environ.get('CLOUDINARY_API_KEY'),
        'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET'),
    }
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#django-allauth settings
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS =2
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 86400 #1 day

ACCOUNT_LOGOUT_REDIRECT_URL = '/accounts/login/' 
LOGIN_REDIRECT_URL = '/accounts/profile/'

# Heroku settings
#django_heroku.settings(locals())
options = DATABASES['default'].get('OPTIONS', {})
options.pop('sslmode', None)


SUMMERNOTE_THEME = 'bs4'

PWA_APP_NAME = 'Rentio'
PWA_APP_DESCRIPTION = "Your partner in Real Estate Mgt"
PWA_APP_THEME_COLOR = '#0A0302'
PWA_APP_BACKGROUND_COLOR = '#ffffff'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'any'
PWA_APP_START_URL = '/'
PWA_APP_STATUS_BAR_COLOR = 'default'
PWA_APP_ICONS = [
    {
        'src': '/static/img/android-chrome-192x192.png',
        'sizes': '192x192'
    }
]
PWA_APP_ICONS_APPLE = [
    {
        'src': '/static/images/my_apple_icon.png',
        'sizes': '160x160'
    }
]
PWA_APP_SPLASH_SCREEN = [
    {
        'src': '/static/images/icons/splash-640x1136.png',
        'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)'
    }
]
PWA_APP_DIR = 'ltr'
PWA_APP_LANG = 'en-US'
