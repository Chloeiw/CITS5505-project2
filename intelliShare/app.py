from flask import Flask, render_template, redirect, url_for, session
from db import db
from models import User
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///IntelliShare.db"
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    #[TODO]
    return render_template('index.html', title="IntelliShare")

@app.route('/login', methods=['GET', 'POST'])
def login():
    #[TODO]
    return "<h2>login</h2>"

@app.route('/register', methods=['GET', 'POST'])
def register():
    #[TODO]
    return "<h2>Register</h2>"

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for(home))



@app.route('/question', methods=['GET'])
def question():
    #[TODO]
    return "<h2>Question</h2>"












if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
