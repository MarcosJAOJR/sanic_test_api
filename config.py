'''Configurations file'''
import os

# Statement for enabling the development environment
DEBUG = os.getenv('DEBUG', True)

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database
DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///' + os.path.join(BASE_DIR, 'app.db'))
DATABASE_CONNECT_OPTIONS = {}
