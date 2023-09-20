import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-salainen'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE = 3
    LANGUAGES = ['en', 'fi']
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')
    MS_TRANSLATOR_REGION = os.environ.get('MS_TRANSLATOR_REGION') or 'northeurope'