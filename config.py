import os
class Config:
   '''
   General configuration parent class
   '''
   pass
   # simple mde  configurations
   SIMPLEMDE_JS_IIFE = True
   SIMPLEMDE_USE_CDN = True
   UPLOADED_PHOTOS_DEST ='app/static/photos'
   SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
   SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://fatuma:qwerty12@localhost/tuma00'
   #  email configurations
   # MAIL_SERVER = 'smtp.googlemail.com'
   # MAIL_PORT = 587
   # MAIL_USE_TLS = True
   # MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
   # MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
class ProdConfig(Config):
   '''
   Production  configuration child class
   Args:
       Config: The parent configuration class with General configuration settings
   '''
   SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://fatuma:qwerty12@localhost/tuma00'
   # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
class TestConfig(Config):
   SQLALCHEMY_DATABASE_URI = 'ppostgresql+psycopg2://fatuma:qwerty12@localhost/tuma_test'
class DevConfig(Config):
   '''
   Development  configuration child class
   Args:
       Config: The parent configuration class with General configuration settings
   '''
config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
