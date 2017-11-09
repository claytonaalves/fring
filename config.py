import os


class BaseConfig:
    DEBUG = True

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    DATABASE_HOST = os.environ['DATABASE_HOST']
    DATABASE_NAME = os.environ['DATABASE_NAME']
    DATABASE_USER = os.environ['DATABASE_USER']
    DATABASE_PASS = os.environ['DATABASE_PASS']

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql://{0}:{1}@{2}/{3}'.format(
        DATABASE_USER,
        DATABASE_PASS,
        DATABASE_HOST,
        DATABASE_NAME
    )
    DATABASE_CONNECT_OPTIONS = {}

    # Application threads. A common general assumption is
    # using 2 per available processor cores - to handle
    # incoming requests using one and performing background
    # operations using the other.
    THREADS_PER_PAGE = 2

    # Enable protection agains *Cross-site Request Forgery (CSRF)*
    CSRF_ENABLED = True

    # Use a secure, unique and absolutely secret key for
    # signing the data.
    CSRF_SESSION_KEY = "mysecretkey"

    # Secret key for signing cookies
    SECRET_KEY = "mysecretkey"

    BABEL_DEFAULT_LOCALE = 'pt_BR'
    # BABEL_DEFAULT_TIMEZONE = ??

    ADVERTISER_MEDIA_PATH = "/srv/images/anunciantes"
    PUBLICATION_MEDIA_PATH = "/srv/images/publicacoes"



class AppConfig(BaseConfig):
    APPLICATION_ROOT = '/app'


class ApiConfig(BaseConfig):
    APPLICATION_ROOT = '/api'


class AdminConfig(BaseConfig):
    APPLICATION_ROOT = '/admin'
