# from io import BytesIO # deprecated
from flask import Flask, request, render_template, session, redirect, url_for
from flask_session import Session  # You might need to install this package
# from flask_sqlalchemy import SQLAlchemy # deprecated

from werkzeug.utils import secure_filename

import os
import chatbot

app = Flask(__name__)

# session configuration
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

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
    return render_template('upload-db.html')

@app.route("/select-sample-db/<db_name>")
def select_sample_db(db_name):
    # Remove the extension from db_name if it has one
    base_name = db_name.rsplit('.', 1)[0]

    # Check for various allowed database file extensions
    for ext in ALLOWED_EXTENSIONS:
        sample_db_filename = f"{base_name}.{ext}"
        sample_db_path = os.path.join('db_sample', sample_db_filename)
        if os.path.isfile(sample_db_path):
            session['db_path'] = sample_db_path
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