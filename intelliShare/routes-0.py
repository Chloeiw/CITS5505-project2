from flask import render_template, redirect, url_for, session
from app import app
from datetime import datetime

@app.route('/')
def home():
    #[TODO]
    posts = [
        {
            'question': 'What is the smartest animal?',
            'username': 'John',
            'timestamp': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
            'content': 'Pantabangan town was submerged in the 1970s to build a reservoir...'
        },

    ]
    return render_template('index.html', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    #[TODO]
    return "<h2>login</h2>"

@app.route('/register', methods=['GET', 'POST'])
def register():
    #[TODO]
    return "<h2>Register</h2>"

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for(home))


# create new question
@app.route('/question', methods=['GET', 'POST'])
def question():
    #[TODO]
    return "<h2>Question</h2>"


@app.route('/answer', methods=['GET', 'POST'])
def answer():
    #[TODO]
    return "<h2>Question</h2>"


@app.route('/search', methods=['GET', 'POST'])
def search():
    #[TODO]
    # Your code here
    return render_template('search.html')
