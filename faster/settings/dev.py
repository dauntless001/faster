from faster.settings.base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-9m2n%wj1zhmevqk9f*blux)m&ml(&p6jk=q62ps#$&101c93jz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'faster.db',
    }


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    Path.cwd().joinpath(BASE_DIR).joinpath('faster/assets'),
]

STATIC_ROOT = Path.cwd().joinpath(BASE_DIR).joinpath('assets')

MEDIA_URL = '/media/'
MEDIA_ROOT = Path.cwd().joinpath(BASE_DIR).joinpath('media')