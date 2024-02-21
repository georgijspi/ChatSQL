from flask import Blueprint, render_template, session, redirect, url_for, request, send_file
from database import db, SampleDatabase
import os
from chatbot import ChatbotProcessor
from werkzeug.utils import secure_filename

def allowed_file(filename, app):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

class RateLimitError(Exception):
    pass

# Define routes
def create_routes_blueprint(app):
    routes = Blueprint('routes', __name__)

    # Routes
    # Landing Page
    @routes.route("/")
    def index():
        return render_template("index.html")

    # Route for uploading database file
    @routes.route("/upload-db", methods=['GET', 'POST'])
    def upload_db():
        sample_databases = SampleDatabase.query.all()
        
        if request.method == 'POST':
            # Check if the post request has the file part
            file = request.files.get('file')
            if not file or file.filename == '':
                return render_template('upload-db.html', sample_databases=sample_databases)
            if file.filename == '':
                return render_template('upload-db.html', sample_databases=sample_databases)
            if file and allowed_file(file.filename, app):
                filename = file.filename
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                session['db_path'] = filepath

                # Clear memory and chat session
                processor = ChatbotProcessor(filepath)
                processor.reset_memory()
                sample_content = processor.generate_sample_content()
                session['sample_content'] = sample_content
                session.pop('conversation', None)
                return redirect(url_for('routes.chat', sample_content=sample_content))
            
        return render_template('upload-db.html', sample_databases=sample_databases)

    @routes.route("/select-sample-db/<db_name>")
    def select_sample_db(db_name):
        session.pop('db_path', None)
        session.pop('conversation', None)
        session.pop('sample_content', None)
        
        # Query the database for the sample database with the given name
        sample_db = SampleDatabase.query.filter_by(name=db_name).first()

        # Initialize the chatbot processor with the sample database
        processor = ChatbotProcessor(sample_db.path)
        processor.reset_memory()
        if sample_db and os.path.isfile(sample_db.path):
            session['db_path'] = sample_db.path
            return redirect(url_for('routes.chat'))

        return "Sample database not found.", 404

    @routes.route("/chat", methods=["GET", "POST"])
    def chat():
        
        db_path = session.get('db_path')
        # if no database is uploaded, redirect to the upload page
        if not db_path or not os.path.isfile(db_path):
            return redirect(url_for('routes.upload_db'))
        
        allow_db_edit = session.get('allow_db_edit', False)

        if request.method == "POST":
            user_message = request.form["message"]
            allow_db_edit = request.form.get("allow_db_edit_hidden", "false") == "true"
            db_path = session.get('db_path', 'chinook.db') 

            print("Allow DB Edit:", allow_db_edit)

            processor = ChatbotProcessor(db_path, allow_db_edit=allow_db_edit)
            
            try:
                bot_response = processor.process_message(user_message)
            except RateLimitError as e:
                return render_template("rate_limit_error.html", error=str(e)) # not implemented yet

            # Update conversation history
            if 'conversation' not in session:
                session['conversation'] = []
            session['conversation'].append({"type": "user", "text": user_message})
            session['conversation'].append({"type": "bot", "text": bot_response})
            session.modified = True

        # Pass the sample_db variable to the template context
        sample_db = SampleDatabase.query.filter_by(path=session.get('db_path')).first()
        if sample_db:
            # Read the HTML file for the description
            with open(sample_db.description_path, 'r') as file:
                description_html = file.read()
        else:
            description_html = None

        # Retrieve generated sample content if present
        if session.get('sample_content'):
            return render_template("chat.html", 
                            conversation=session.get('conversation', []),
                            sample_db=sample_db,
                            description_html=description_html,
                            sample_content=session['sample_content'])
        else:
            return render_template("chat.html", 
                            conversation=session.get('conversation', []),
                            sample_db=sample_db,
                            description_html=description_html)

    @routes.route("/download-db")
    def download_db():
        db_path = session.get('db_path')
        if db_path and os.path.isfile(db_path):
            return send_file(db_path, as_attachment=True)
        return "No database available for download.", 404

    return routes
