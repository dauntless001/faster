from faster.settings.base import *
import os, dj_database_url
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'False') == 'True'

DATABASES['default'] = dj_database_url.parse(
    url = os.getenv('DATABASE_URL'), conn_max_age=600
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    Path.cwd().joinpath(BASE_DIR).joinpath('faster/assets'),
]

STATIC_ROOT = Path.cwd().joinpath(BASE_DIR).joinpath('assets')

MEDIA_URL = '/media/'
MEDIA_ROOT = Path.cwd().joinpath(BASE_DIR).joinpath('media')