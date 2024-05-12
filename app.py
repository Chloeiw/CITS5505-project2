from flask import Flask, render_template, request, url_for

app = Flask(__name__, static_url_path='/static')

# Define routes
@app.route('/')
def index():
    return render_template('addQuestion_v1.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        title = request.form['title']
        subtitle = request.form['subtitle']
        question = request.form['question']
        print(f'Title: {title}, Subtitle: {subtitle}, Question: {question}')
        return 'Question submitted successfully!'

if __name__ == '__main__':
    app.run(debug=True)
