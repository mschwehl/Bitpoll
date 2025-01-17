import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# customize to your needs

# You must insert your own random value here
# SECURITY WARNING: keep the secret key used in production secret!
# see <https://docs.djangoproject.com/en/dev/howto/deployment/checklist/#secret-key>
SECRET_KEY = '..'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['*']

FIELD_ENCRYPTION_KEY = "this+is+an+example+key+please+generate+one+="

## If Bitpoll is served via HTTPS enable the next two options
#SESSION_COOKIE_SECURE = True
#CSRF_COOKIE_SECURE = True


#Add additionall installed apps here
## Example for installed raven (Sentry instrumentation)
#INSTALLED_APPS_LOCAL = [
#        'raven.contrib.django.raven_compat',
#        ]
INSTALLED_APPS_LOCAL = []

# Compress the JS and CSS files, for more Options see https://django-pipeline.readthedocs.io/en/latest/compressors.html
# the Compressor have to be installed in the system
PIPELINE_LOCAL = {}
#PIPELINE_LOCAL['JS_COMPRESSOR'] = 'pipeline.compressors.uglifyjs.UglifyJSCompressor'
#PIPELINE_LOCAL['CSS_COMPRESSOR'] = 'pipeline.compressors.cssmin.CSSMinCompressor'
#PIPELINE_ENABLED = True

LANGUAGE_CODE = 'de-de'
TIME_ZONE = 'Europe/Berlin'

## https://docs.djangoproject.com/en/1.9/ref/settings/#databases
## Use settings from docker-compose here if starting with docker-compose
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '192.168.99.101',
        'PORT': '5000',
    }
}

## Customize your instance
SITE_NAME = 'Bitpoll'
BASE_URL = 'https://bitpoll.example.com'

## Url to the Base Homepage and Text on the Link, leave empty to not use this option
HOME_URL = "https://example.com"
HOME_URL_NAME = "Dashboard"

MEDIA_ROOT = os.path.join(ROOT_DIR, '_media')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(ROOT_DIR, '_static')
STATIC_URL = '/static/'
LOGIN_REDIRECT_URL = "/"

## Test mail functionality by printing mails to console:
## EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
## Only use one of them with True: EMAIL_USE_SSL, EMAIL_USE_TLS

EMAIL_HOST = 'mail.example.com'
EMAIL_HOST_PASSWORD = 'pass'
EMAIL_HOST_USER	= 'host'
EMAIL_PORT = 587
EMAIL_SUBJECT_PREFIX = '[Bitpoll] '
EMAIL_USE_SSL = False
EMAIL_USE_TLS = True
FILE_CHARSET = 'utf-8'
SERVER_EMAIL = 'server@example.com'
MAIL_SIGNATURE = "Bitpoll Team"
TEAM_EMAIL = "server@example.com"

## if the imprint URL is not empty use it as an link to the imprint, else use IMPRINT_TEXT
#IMPRINT_URL = ""
#IMPRINT_TEXT = """
#<h1>ImpressuXm</h1>
#<p>Text goes here</p>
#"""

#LOCALE_PATHS = (os.path.join(ROOT_DIR, 'locale'), )
#LANGUAGES = (
#    ('de', 'Deutsch'),
#    ('en', 'English'),
#    #('fr', 'Français'),
#)

REGISTER_ENABLED = True
GROUP_MANAGEMENT = REGISTER_ENABLED

## Use ldap login
#import ldap
#from django_auth_ldap.config import LDAPSearch
#
#AUTHENTICATION_BACKENDS = (
#    'django_auth_ldap.backend.LDAPBackend',
#    'django.contrib.auth.backends.ModelBackend',
#    )
#
#AUTH_LDAP_SERVER_URI = "ldap_host"
#AUTH_LDAP_BIND_DN = "ldap_bind_dn"
#AUTH_LDAP_BIND_PASSWORD = "ldap_bind_pw"
#AUTH_LDAP_USER_SEARCH = LDAPSearch("ou=People,dc=mafiasi,dc=de",
#    ldap.SCOPE_SUBTREE, "(uid=%(user)s)")
#AUTH_LDAP_ALWAYS_UPDATE_USER = True
#
#from django_auth_ldap.config import LDAPSearch, PosixGroupType
#
#AUTH_LDAP_GROUP_SEARCH = LDAPSearch("ou=groups,dc=mafiasi,dc=de",
#    ldap.SCOPE_SUBTREE, "(objectClass=posixGroup)"
#    )
#AUTH_LDAP_GROUP_TYPE = PosixGroupType()
##AUTH_LDAP_FIND_GROUP_PERMS = True
#AUTH_LDAP_MIRROR_GROUPS = True
#
#AUTH_LDAP_USER_ATTR_MAP = {"first_name": "givenName", "last_name": "sn", "email": "mail"}
#
#AUTH_LDAP_USER_FLAGS_BY_GROUP = {
#    "is_staff": ["cn=Editoren,ou=groups,dc=mafiasi,dc=de",
#                 "cn=Server-AG,ou=groups,dc=mafiasi,dc=de"],
#    "is_superuser": "cn=Server-AG,ou=groups,dc=mafiasi,dc=de"
#}
