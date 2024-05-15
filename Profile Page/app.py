from flask import Flask, render_template, request, url_for

app = Flask(__name__, static_url_path='/static')

# Define routes
@app.route('/')
def index():
    return render_template('profile.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
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

if __name__ == '__main__':
    app.run(debug=True)