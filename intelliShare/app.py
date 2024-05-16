from flask import Flask
from routes import configure_routes

app = Flask(__name__, static_url_path='/static')

# Configure upload folder and allowed extensions
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload directory exists
import os
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Call the function to configure routes
configure_routes(app)

if __name__ == '__main__':
    app.run(debug=True)