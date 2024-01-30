from flask import Flask, request, render_template, session
from flask_session import Session  # You might need to install this package
import chatbot

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    # Route for the landing page
    return render_template("index.html")

@app.route("/chat", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        user_message = request.form["message"]
        bot_response = chatbot.process_chat_message(user_message)

        # Update conversation history
        if 'conversation' not in session:
            session['conversation'] = []
        session['conversation'].append({"type": "user", "text": user_message})
        session['conversation'].append({"type": "bot", "text": bot_response})

    return render_template("chat.html", conversation=session.get('conversation', []))

if __name__ == "__main__":
    app.run(debug=True)
