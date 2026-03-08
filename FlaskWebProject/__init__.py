"""
The Flask application package with MSAL, database, login, and session support.
"""
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session
from config import Config

# ------------------ APP INITIALIZATION ------------------ #
app = Flask(__name__)
app.config.from_object(Config)

# Secret key for session & CSRF
app.secret_key = app.config.get('SECRET_KEY', 'supersecretkey')

# Enable server-side sessions (for MSAL token cache)
Session(app)

# Setup SQLAlchemy ORM
db = SQLAlchemy(app)

# Setup Flask-Login
login = LoginManager(app)
login.login_view = 'login'

# ------------------ LOGGING ------------------ #
if not app.debug:
    # Log to stderr in production
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    app.logger.info("Flask app initialized with MSAL integration.")

# ------------------ IMPORT VIEWS ------------------ #
# Must be imported after app, db, login are defined
import FlaskWebProject.views
