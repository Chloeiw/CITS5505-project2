from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title="IntelliShare")

@app.route('/login')
def login():
    return "<h2>login</h2>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
