# from io import BytesIO # deprecated
from flask import Flask, request, render_template, session, redirect, url_for
from flask_session import Session  # You might need to install this package
from flask_sqlalchemy import SQLAlchemy 

from werkzeug.utils import secure_filename

import os
import chatbot

from model import db, SampleDatabase

app = Flask(__name__)

# session configuration
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sample_databases.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Command to initialize the database
@app.cli.command('init-db')
def init_db():
    db.create_all()
    print("Initialized the database.")

# Command to populate the database with sample databases
@app.cli.command('populate-db')
def populate_db():
    # List of sample databases
    sample_dbs = [
        {'name': 'Covid Vaccination Information', 'description_path': "db-descriptions/sampleDB-1.html", 'path': 'db_sample/sample_1.sqlite3'},
        {'name': 'Interactive Clue-Style Mystery Game Database', 'description_path': "db-descriptions/sampleDB-2.html", 'path': 'db_sample/sample_2.sqlite3'},
        {'name': "World's Tallest Buildings Database", 'description_path': "db-descriptions/sampleDB-3.html", 'path': 'db_sample/sample_3.sqlite3'},
        {'name': 'Comprehensive Music Store Database', 'description_path': "db-descriptions/sampleDB-4.html", 'path': 'db_sample/sample_4.db'},
        # Add more samples as needed
    ]

    for sample_db in sample_dbs:
        db_entry = SampleDatabase(name=sample_db['name'], 
                                  description_path=sample_db['description_path'], 
                                  path=sample_db['path'])
        db.session.add(db_entry)
    
    db.session.commit()
    print("Sample databases added to the database.")

# database configuration
UPLOAD_FOLDER = 'db_uploads'  # Make sure this directory exists
ALLOWED_EXTENSIONS = {'db', 'sqlite', 'sqlite3'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Helper function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# routes
@app.route("/")
def index():
    # Route for the landing page
    return render_template("index.html")

# Route for uploading database file
@app.route("/upload-db", methods=['GET', 'POST'])
def upload_db():
    if request.method == 'POST':
        # Check if the post request has the file part
        file = request.files.get('file')
        if not file:
            return render_template('upload_db.html', error="No file part in the request")
        if file.filename == '':
            return render_template('upload_db.html', error="No selected file")
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            session['db_path'] = filepath
            return redirect(url_for('chat'))

    sample_databases = SampleDatabase.query.all()
    return render_template('upload-db.html', sample_databases=sample_databases)

@app.route("/select-sample-db/<db_name>")
def select_sample_db(db_name):
    # Query the database for the sample database with the given name
    sample_db = SampleDatabase.query.filter_by(name=db_name).first()

    if sample_db and os.path.isfile(sample_db.path):
        session['db_path'] = sample_db.path
        return redirect(url_for('chat'))

    return "Sample database not found.", 404


@app.route("/chat", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        user_message = request.form["message"]
        db_path = session.get('db_path', 'chinook.db')  # Use the uploaded database if available
        bot_response = chatbot.process_chat_message(user_message, db_path)

        # Update conversation history
        if 'conversation' not in session:
            session['conversation'] = []
        session['conversation'].append({"type": "user", "text": user_message})
        session['conversation'].append({"type": "bot", "text": bot_response})

    return render_template("chat.html", conversation=session.get('conversation', []))

if __name__ == "__main__":
    app.run(debug=True)

# File download and upload code taken from : https://www.geeksforgeeks.org/uploading-and-downloading-files-in-flask/