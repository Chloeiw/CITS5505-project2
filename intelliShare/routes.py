import requests
from datetime import datetime
from flask import request, render_template, redirect, session, url_for, Blueprint
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from .models import User

main = Blueprint("main", __name__)



@main.route('/')
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


@main.route('/login', methods=['GET', 'POST'])
def login():
    #[TODO]
    return "<h2>login</h2>"

@main.route('/register', methods=['GET', 'POST'])
def register():
    #[TODO]
    return "<h2>Register</h2>"

@main.route('/logout')
@login_required
def logout():
    session.pop('username', None)
    return redirect(url_for(home))


# create new question
@main.route('/question', methods=['GET', 'POST'])
@login_required
def question():
    #[TODO]
    return "<h2>Question</h2>"


@main.route('/answer', methods=['GET', 'POST'])
@login_required
def answer():
    #[TODO]
    return "<h2>Question</h2>"


@main.route('/search', methods=['GET', 'POST'])
def search():
    #[TODO]
    # Your code here
    return render_template('search.html')
