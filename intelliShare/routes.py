from datetime import datetime
from flask import jsonify, request, render_template, redirect, session, url_for, Blueprint, flash
from flask_login import login_user, login_required, logout_user

from werkzeug.security import generate_password_hash, check_password_hash
from .models import Question, User

main = Blueprint("main", __name__)



@main.route('/')
def home():
    posts = get_posts_from_database(0, 2)
    return render_template('index.html', posts=posts)


class Post:
    def __init__(self, question_id, question, username, timestamp, content):
        self.question_id = question_id
        self.question = question
        self.username = username
        self.timestamp = timestamp
        self.content = content

def get_posts_from_database(start, limit):
    all_posts = [
        Post(1, 'What is the smartest animal?', 'John', datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'), 'Pantabangan town was submerged in the 1970s to build a reservoir...'),
        Post(2, 'What is the smartest animal?', 'John', datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'), 'Pantabangan town was submerged in the 1970s to build a reservoir...'),
        Post(3, 'What is the smartest animal?', 'John', datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'), 'Pantabangan town was submerged in the 1970s to build a reservoir...'),
        Post(4, 'What is the smartest animal?', 'John', datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'), 'Pantabangan town was submerged in the 1970s to build a reservoir...')
    ]
    return all_posts[start:start+limit]

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
    return redirect(url_for("main.home"))


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


@main.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    #[TODO]
    return "<h2>profile</h2>"

    # Route to display question details and answers
@main.route('/questionDetails_v1/<int:question_id>')
def question_details(question_id):
    question = next((q for q in questions if q['id'] == question_id), None)
    if not question:
        return "Question not found", 404
    question_answers = [a for a in answers if a['question_id'] == question_id]
    return render_template('questionDetails_v1.html', question=question, answers=question_answers)

@main.route('/search', methods=['GET', 'POST'])
def search():
    query = request.args.get('query')
    results = []

    if query:  # only search if a query is provided
        all_posts = get_posts_from_database(0, 100)  # get all posts
        results = [post for post in all_posts if query in post.question]  # search in post question

        if not results:
            flash('No results found!')

    return render_template('search.html', results=results)

