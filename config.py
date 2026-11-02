# config.py
import os
from datetime import timedelta

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Essential cryptographic key for user sessions/cookies
    SECRET_KEY = os.environ.get('SECRET_KEY', 'khatri_agrovet_secure_dev_key_1024')
    
    # Path to local SQLite relational database file
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'khatri_agrovet.db')
    
    # Disable tracking system overhead to keep performance fast
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Auto-expires login sessions after 30 minutes of inactivity
    REMEMBER_COOKIE_DURATION = timedelta(minutes=30)