import os


# Creates the default Config Object
class Config(object):
    APP_TITLE = "#FirdayNight"  # This is just a placeholder
    MAP_KEY = os.environ['MAP_API']
    DEBUG = False
    TESTING = False
    DATABASE_URI = ""


# Overrides the default Config Object for Production
class ProductionConfig(Config):
    DATABASE_URI = ""


# Overrides the default Config Object for Development
class DevelopmentConfig(Config):
    DEBUG = True


# Overrides the default Config Object for Testing
class TestingConfig(Config):
    TESTING = True


del os
