import os
from dotenv import load_dotenv

import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'
    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT')
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER')
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY')
    BLOB_CONNECTION_STRING = os.environ.get('BLOB_CONNECTION_STRING')

    SQL_SERVER = os.environ.get('SQL_SERVER')
    SQL_DATABASE = os.environ.get('SQL_DATABASE')
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME')
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = f"mssql+pyodbc://{SQL_USER_NAME}@{SQL_SERVER}:{SQL_PASSWORD}@{SQL_SERVER}:1433/{SQL_DATABASE}?driver=ODBC+Driver+17+for+SQL+Server"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CLIENT_ID = os.environ.get('CLIENT_ID')
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
    AUTHORITY = "https://login.microsoftonline.com/2ed5a947-68e8-47c7-ba73-1a6b5617b15e"
    REDIRECT_PATH = "/getAToken"
    SCOPE = ["User.Read"]
    SESSION_TYPE = "filesystem"
