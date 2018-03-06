import os


_basedir = os.path.abspath(os.path.dirname(__file__))


# Creates the default Config Object
class Config(object):
    # APP Settings
    APP_TITLE = "#FirdayNight"  # This is just a placeholder
    DEBUG = False
    TESTING = False

    SECRET_KEY = "testing_secret_key"

    # API Keys
    GOOGLE_MAP_KEY = os.environ['MAP_API']

    # database configuration
    DATABASE_URI = "sqlite:///:memory:"


# Overrides the default Config Object for Production
class ProductionConfig(Config):
    DATABASE_URI = os.path.join(_basedir, "MWMFlask.db")


# Overrides the default Config Object for Development
class DevelopmentConfig(Config):
    DEBUG = True

    DATABASE_URI = os.path.join(_basedir, "MWMFlask.db")


# Overrides the default Config Object for Testing
class TestingConfig(Config):
    TESTING = True

    # database configuration
    DATABASE_URI = os.path.join(_basedir, "TestDB.db")


del os
