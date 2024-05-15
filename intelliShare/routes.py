from flask import render_template, redirect, url_for, session
from app import app

@app.route('/')
def home():
    #[TODO]
    return render_template('index.html', title="IntelliShare")

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
    return "<h2>search</h2>"


