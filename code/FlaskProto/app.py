from flask import Flask
from flask_session import Session
from database import db, SampleDatabase
from routes import create_routes_blueprint

app = Flask(__name__)
app.config.from_pyfile('config.py')
Session(app)
db.init_app(app)


# Register routes with the app
app.register_blueprint(create_routes_blueprint(app))

# Command to initialize the database
@app.cli.command('init-db')
def init_db():
    db.create_all()
    print("Initialized the database.")

# Command to populate the SQLAlchemy database with sample databases
@app.cli.command('populate-db')
def populate_db():
    sample_dbs = [
        {'name': 'Covid Vaccination Information', 'description_path': "db-descriptions/sampleDB-1.html", 'path': 'db_sample/sample_1.sqlite3'},
        {'name': 'Interactive Clue-Style Mystery Game Database', 'description_path': "db-descriptions/sampleDB-2.html", 'path': 'db_sample/sample_2.sqlite3'},
        {'name': "World's Tallest Buildings Database", 'description_path': "db-descriptions/sampleDB-3.html", 'path': 'db_sample/sample_3.sqlite3'},
        {'name': 'Comprehensive Music Store Database', 'description_path': "db-descriptions/sampleDB-4.html", 'path': 'db_sample/sample_4.db'},
    ]

    for sample_db in sample_dbs:
        db_entry = SampleDatabase(name=sample_db['name'], 
                                  description_path=sample_db['description_path'], 
                                  path=sample_db['path'])
        db.session.add(db_entry)
    
    db.session.commit()
    print("Sample databases added to the database.")

if __name__ == "__main__":
    app.run(debug=True)
