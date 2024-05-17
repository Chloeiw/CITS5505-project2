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


def get_posts_from_database(start, limit):
    # This is a placeholder function. Replace it with actual database query later.
    # return Post.query.order_by(Post.timestamp.desc()).offset(start).limit(limit).all()
    all_posts = [
        {
            'question_id': 1,
            'question': 'What is the smartest animal?',
            'username': 'John',
            'timestamp': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
            'content': 'Pantabangan town was submerged in the 1970s to build a reservoir...'
        },
        {
            'question_id': 2,
            'question': 'What is the smartest animal?',
            'username': 'John',
            'timestamp': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
            'content': 'Pantabangan town was submerged in the 1970s to build a reservoir...'
        },
        {
            'question_id': 3,
            'question': 'What is the smartest animal?',
            'username': 'John',
            'timestamp': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
            'content': 'Pantabangan town was submerged in the 1970s to build a reservoir...'
        },
        {
            'question_id': 4,
            'question': 'What is the smartest animal?',
            'username': 'John',
            'timestamp': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
            'content': 'Pantabangan town was submerged in the 1970s to build a reservoir...'
        }
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


@main.route('/search', methods=['GET', 'POST'])
def search():
    search_query = request.args.get('query')
    search_results=[]
    if search_query:
            # Use the search_query to make a query to the database
            search_results = Question.query.filter(Question.title.contains(search_query)).all()
            # Check if search_results is empty
            if not search_results:
                error_message = "No matching questions found."
                flash(error_message)
    # Render a template and pass the search results to it

        
    return render_template('search.html', results=search_results)


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

@main.route('/get_posts')
def get_posts():
    start = request.args.get('start', 0, type=int)
    limit = request.args.get('limit', 3, type=int)
    posts = get_posts_from_database(start, limit)
    return jsonify(posts)
