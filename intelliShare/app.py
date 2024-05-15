from flask import Flask
from db import db
from models import User
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///IntelliShare.db"
db.init_app(app)

with app.app_context():
    db.create_all()



from routes import *







if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
