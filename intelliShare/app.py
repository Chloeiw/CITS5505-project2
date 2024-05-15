from flask import Flask, render_template
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///../db/IntelliShare.db'
db.init_app(app)


@app.route('/')
def home():
    return render_template('index.html', title="IntelliShare")

@app.route('/login')
def login():
    return "<h2>login</h2>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
