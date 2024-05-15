from flask import Flask, render_template
from db import db
from models import User
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///IntelliShare.db"
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    # user = User(username="changkai", password="123", image="default")
    # db.session.add(user)
    # db.session.commit()
    return render_template('index.html', title="IntelliShare")

@app.route('/login')
def login():
    return "<h2>login</h2>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
