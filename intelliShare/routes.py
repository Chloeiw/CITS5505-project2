from flask import render_template, request, redirect, url_for, send_from_directory, jsonify, flash, session
from datetime import datetime
import os
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import desc

questions = []
answers = []
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
# Check if the uploaded file is allowed
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def configure_routes(app, db):

    # 用户模型
    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(50), unique=True, nullable=False)
        password = db.Column(db.String(200), nullable=False)

    # 登录路由
    @app.route('/login', methods=['POST'])
    def login():
        data = request.json
        username = data.get('username')
        password = data.get('password')
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            return jsonify({"message": "Login successful", "username": user.username}), 200
        return jsonify({"message": "Invalid username or password"}), 401

    # 注册路由
    @app.route('/signup', methods=['POST'])
    def signup():
        data = request.json
        username = data.get('username')
        password = data.get('password')
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created successfully"}), 201

    # Route for the main page where questions can be added
    @app.route('/add')
    def addQuestion():
        return render_template('addQuestion_v1.html')

    # Route to handle question submissions
    @app.route('/submit_question', methods=['POST'])
    def submit_question():
        title = request.form['title']
        subtitle = request.form['subtitle']
        question = request.form['question']
        username = "Andrianto Hadi"  # This should be dynamically set based on the current user in a real app
        submission_time = datetime.now().strftime('%d %b %Y %H:%M:%S')
        question_id = len(questions) + 1
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

    # Route to display question details and answers
    @app.route('/questionDetails_v1/<int:question_id>')
    def question_details(question_id):
        question = next((q for q in questions if q['id'] == question_id), None)
        if not question:
            return "Question not found", 404
        question_answers = [a for a in answers if a['question_id'] == question_id]
        return render_template('questionDetails_v1.html', question=question, answers=question_answers)

    # Route to handle answer submissions
    @app.route('/questionDetails_v1', methods=['POST'])
    def submit_answer():
        question_id = int(request.form['question_id'])
        answer_text = request.form['answer']
        username = "Andrianto Hadi"  # This should be dynamically set based on the current user in a real app
        submission_time = datetime.now().strftime('%d %b %Y %H:%M:%S')
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
        return redirect(url_for('question_details', question_id=question_id))

    # Serve uploaded files
    @app.route('/uploads/<filename>')
    def uploaded_file(filename):
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

    # Profile route
    @app.route('/profile')
    def profile():
        return render_template('profile.html')

    # Route to handle profile submission
    @app.route('/submit_profile', methods=['POST'])
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
    
    @app.route('/')
    def home():
        return render_template('index.html')
    #    posts = get_posts_from_database(0, 2)
    #   return render_template('index.html', posts=posts)


    #def get_posts_from_database(start, limit):
    #    all_posts = Question.query.order_by(desc(Question.post_time)).all()  # get all posts ordered by timestamp
    #   return all_posts[start:start+limit]
    
    @app.route('/search', methods=['GET', 'POST'])
    def search():
        query = request.args.get('query')
        results = []

        if query:  # only search if a query is provided
            all_posts = get_posts_from_database(0, 100)  # get all posts
            results = [post for post in all_posts if query in post.title]  # search in post title

            if len(results)==0 :
                flash('No results found!')

        return render_template('search.html', results=results)