from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class SampleDatabase(db.Model):
    __tablename__ = 'sample_databases'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description_path = db.Column(db.String(200), unique=True, nullable=False)
    path = db.Column(db.String(200), unique=True, nullable=False)

    def __repr__(self):
        return f'<SampleDatabase {self.name}>'
