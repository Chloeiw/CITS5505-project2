from datetime import datetime
from flask import flash, redirect, render_template, request, url_for
from intelliShare import flaskApp

@flaskApp.route("/")
@flaskApp.route("/index")
def index():
    posts = [
        {
            'question': 'What is the smartest animal?',
            'username': 'John',
            'timestamp': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
            'content': 'Pantabangan town was submerged in the 1970s to build a reservoir...'
        },

    ]
    return render_template('index.html', posts=posts)

@flaskApp.route("/search")
def search():
    # Your code here
    return render_template('search.html')

if __name__ == "__main__":
    flaskApp.run(debug=True)