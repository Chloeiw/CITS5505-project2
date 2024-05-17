from datetime import datetime
from flask import jsonify, request, render_template, redirect, session, url_for, Blueprint, flash
from flask_login import login_user, login_required, logout_user
import os
from werkzeug.security import generate_password_hash, check_password_hash
from .models import Question, User

main = Blueprint("main", __name__)

# Temporary data storage
questions = []
answers = []

# Configure upload folder and allowed extensions
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Ensure the upload directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
# Check if the uploaded file is allowed
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@main.route('/')
def home():
    posts = get_posts_from_database(0, 2)
    return render_template('index.html', posts=posts)


def get_posts_from_database(start, limit):
    all_posts = Question.query.order_by(desc(Question.post_time)).all()  # get all posts ordered by timestamp
    return all_posts[start:start+limit]

@main.route('/login', methods=['GET', 'POST'])
def login():
    #[TODO]
    return "<h2>login</h2>"

@main.route('/register', methods=['GET', 'POST'])
def register():
    #[TODO]
    return "<h2>Register</h2>"

@main.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    session.pop('username', None)
    return redirect(url_for("main.home"))

# create new question
@main.route('/addQuestion_v1', methods=['GET','POST'])
def question():
    if request.method == 'POST':
        title = request.form['title']
        subtitle = request.form['subtitle']
        question = request.form['question']
        username = "Andrianto Hadi"  # This should be dynamically set based on the current user in a real app
        submission_time = datetime.now().strftime('%d %b %Y %H:%M:%S')       
        # Handle file upload
        if 'cover' in request.files:

            file = request.files['cover']
            if file and allowed_file(file.filename):
                filename = file.filename
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)

        question_id = len(questions) + 1
        questions.append({
            'id': question_id,
            'title': title,
            'subtitle': subtitle,
            'question': question,
            'cover': filename,
            'username': username,
            'submission_time': submission_time
        })
        
        return redirect(url_for('question_details', question_id=question_id))

@main.route('/addQuestion_v1.html')
def add():
    return render_template('addQuestion_v1.html')

@main.route('/questionDetails_v1.html')
def details():
    return render_template('questionDetails_v1.html')

# Route to handle answer submissions
@main.route('/questionDetails_v1.html', methods=['GET','POST'])
def answer():
    question_id = int(request.form['question_id'])
    answer_text = request.form['answer']
    answer_time = datetime.now().strftime('%d %b %Y %H:%M:%S')
    answer = {
        'question_id': question_id,
        'text': answer_text,
        'username': "User",  # This should be dynamically set based on the current user in a real app
        'answer_time': answer_time
    }

    # Handle file upload
    if 'file' in request.files:
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = file.filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            answer['image'] = filename

    answers.append(answer)
    return redirect(url_for('question_details'))

@main.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    #[TODO]
    return "<h2>profile</h2>"

# Route to display question details and answers
@main.route('/questionDetails_v1.html/<int:question_id>')
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
        results = [post for post in all_posts if query in post.title]  # search in post title

        if len(results)==0 :
            flash('No results found!')

    return render_template('search.html', results=results)

