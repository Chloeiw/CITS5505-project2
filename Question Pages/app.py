from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from datetime import datetime
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path='/static')

# Configure upload folder and allowed extensions
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Temporary data storage
questions = []
answers = []

# Check if the uploaded file is allowed
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route for the main page where questions can be added
@app.route('/')
def index():
    return render_template('addQuestion_v1.html')

# Route to handle question submissions
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        title = request.form['title']
        subtitle = request.form['subtitle']
        question = request.form['question']
        username = "Andrianto Hadi"  # This should be dynamically set based on the current user in a real app
        submission_time = datetime.now().strftime('%d %b %Y %H:%M:%S')
 
        
        question_id = len(questions) + 1
        questions.append({
            'id': question_id,
            'title': title,
            'subtitle': subtitle,
            'question': question,
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
    return redirect(url_for('question_details', question_id=question_id))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
