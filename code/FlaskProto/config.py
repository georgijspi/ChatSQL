# database configuration
UPLOAD_FOLDER = 'db_uploads'  # Make sure this directory exists
ALLOWED_EXTENSIONS = {'db', 'sqlite', 'sqlite3'}

# flask session configuration
SESSION_PERMANENT = False
SESSION_TYPE = "filesystem"

# SQLAlchemy configuration
SQLALCHEMY_DATABASE_URI = 'sqlite:///sample_databases.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False