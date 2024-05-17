from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from routes import configure_routes

app = Flask(__name__, static_url_path='/static')

# Configure upload folder and allowed extensions
UPLOAD_FOLDER = 'uploads'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Call the function to configure routes
configure_routes(app, db)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
