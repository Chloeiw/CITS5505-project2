from datetime import datetime
from flask import abort, jsonify, request, render_template, redirect, session, url_for, Blueprint, flash, send_from_directory
from flask_login import login_user, login_required, logout_user
import os
from sqlalchemy import desc
from werkzeug.security import generate_password_hash, check_password_hash
from .models import Question, User,Answer
from .db import db

main = Blueprint("main", __name__)

# Temporary data storage
questions = []
answers = []

# Configure upload folder and allowed extensions
PROJ='intelliShare'
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

class Post:
    def __init__(self, question_id, question, username, timestamp, content):
        self.question_id = question_id
        self.question = question
        self.username = username
        self.timestamp = timestamp
        self.content = content

        def to_dict(self):
            return {
                'id': self.id,
                'title': self.title,
                'content': self.content,
                # ... other fields ...
            }

# Function to get posts from the database
def get_posts_from_database(start, limit):
    all_posts = Question.query.order_by(desc(Question.post_time)).all()  # get all posts ordered by timestamp
    return all_posts[start:start+limit]

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print("request post login")
        r = request.get_json()
        username = r['username']
        password = r['password']
        print(username, password)


        user = User.query.filter_by(username=username).first()
        print(user)
        if user and user.password == password:
            login_user(user)
            # return redirect(url_for('profile'))
            return {"status":200, "message":"success"}
        return {"status":400, "message":"user & pwd not match"}
    print("request login get")
    return render_template('index.html')

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
@main.route('/addQuestion_v1', methods=['GET', 'POST'])
def add_question():
    if request.method == 'POST':
        title = request.form['title']
        subtitle = request.form['subtitle']
        question_text = request.form['question']
        user_id = 'user_id'
        username = 'username'
        submission_time = datetime.now().strftime('%d %b %Y %H:%M:%S')
        
        filename = None
        if 'cover' in request.files:
            file = request.files['cover']
            if file and allowed_file(file.filename):
                filename = file.filename
                filepath = os.path.join(PROJ, UPLOAD_FOLDER, filename)
                file.save(filepath)

        question_id = len(questions) + 1
        questions.append({
            'id': question_id,
            'title': title,
            'subtitle': subtitle,
            'question': question_text,
            'cover': filename,
            'username': username,
            'submission_time': submission_time,
            'user_id': user_id
        })
        
        new_question = Question()

        new_question.title = title
        new_question.subtitle = subtitle
        new_question.content = question_text
        new_question.cover = filename
        new_question.post_time = submission_time  
        new_question.user_id = user_id
        new_question.username = username

        db.session.add(new_question)
        db.session.commit()

        return redirect(url_for('main.question_details', question_id=question_id))
    
    return render_template('addQuestion_v1.html')

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
    username = username
    user_id = 'uesr_id'

    new_answer = answer(text=answer_text, answer_time=answer_time, user_id=user_id, question_id=question_id)

    db.session.add(new_answer)
    db.session.commit()

    # Handle file upload
    if 'file' in request.files:
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = file.filename
            filepath = os.path.join(PROJ, UPLOAD_FOLDER, filename)
            file.save(filepath)

            answer['image'] = filename

    answers.append(answer)
    return redirect(url_for('main.question_details', question_id=question_id))

@main.route('/profile', methods=['GET', 'POST'])
def profile():
    return render_template('profile.html')

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
        results = [post for post in all_posts if query in post.title]  # search in post question

        if not results:
            flash('No results found!')

    return render_template('search.html', results=results)



    # Serve uploaded files
@main.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


# Route to handle profile submission
@main.route('/submit_profile', methods=['POST'])
def submit_profile():
    username = request.form['username']
    gender = request.form['gender']
    occupation = request.form['occupation']
    self_intro = request.form['selfIntro']
    password = request.form['password']
    security_question = request.form['securityQuestion']
    security_answer = request.form['securityAnswer']
        
    # Print the received form data
    print(f'Username: {username}')
    print(f'Gender: {gender}')
    print(f'Occupation: {occupation}')
    print(f'Self Introduction: {self_intro}')
    print(f'Password: {password}')
    print(f'Security Question: {security_question}')
    print(f'Security Answer: {security_answer}')
        
    return 'Profile submitted successfully!'
@main.route('/get_more_posts', methods=['GET'])
def get_more_posts():
    start = request.args.get('start', type=int)
    limit = request.args.get('limit', type=int)
    more_questions = get_posts_from_database(start, limit)  # Assuming this function now returns Question objects
    return jsonify([question.to_dict() for question in more_questions])

@main.route('/questioninfo/<int:question_id>')
def question_details_copy(question_id):
    # Fetch the question from the database using question_id
    question = Question.query.get(question_id)
    if question is None:
        abort(404)  # Not found
    answers = Answer.query.filter_by(question_id=question_id).all()
    print(answers)  # Print the answers to the console
    return render_template('questioninfo.html', question=question, answers=answers)


