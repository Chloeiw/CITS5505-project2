from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>HomePage</h1>"


@app.route('/login')
def login():
    return "<h2>login</h2>"







if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
