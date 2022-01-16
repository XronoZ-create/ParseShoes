import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    TG_TOKEN = "TG_TOKEN"  # Your token telegram
    TG_CHAT_ID = 000000000  # Your id telegram chat
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'shoes_database.sqlite')

    SIZE_PARSE = "11"