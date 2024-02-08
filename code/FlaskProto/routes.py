from flask import Blueprint, render_template, session, redirect, url_for, request
from database import db, SampleDatabase
import os
import chatbot
from werkzeug.utils import secure_filename

# Define the allowed_file function here
def allowed_file(filename, app):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Define routes
def create_routes_blueprint(app):
    routes = Blueprint('routes', __name__)

    # routes
    @routes.route("/")
    def index():
        # Route for the landing page
        return render_template("index.html")

    # Route for uploading database file
    @routes.route("/upload-db", methods=['GET', 'POST'])
    def upload_db():
        if request.method == 'POST':
            # Check if the post request has the file part
            file = request.files.get('file')
            if not file:
                return render_template('upload_db.html', error="No file part in the request")
            if file.filename == '':
                return render_template('upload_db.html', error="No selected file")
            if file and allowed_file(file.filename, app):  # Pass 'app' as an argument
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                session['db_path'] = filepath
                return redirect(url_for('routes.chat'))

        sample_databases = SampleDatabase.query.all()
        return render_template('upload-db.html', sample_databases=sample_databases)

    @routes.route("/select-sample-db/<db_name>")
    def select_sample_db(db_name):
        # Query the database for the sample database with the given name
        sample_db = SampleDatabase.query.filter_by(name=db_name).first()

        if sample_db and os.path.isfile(sample_db.path):
            session['db_path'] = sample_db.path
            return redirect(url_for('routes.chat'))

        return "Sample database not found.", 404


    @routes.route("/chat", methods=["GET", "POST"])
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
    return routes
