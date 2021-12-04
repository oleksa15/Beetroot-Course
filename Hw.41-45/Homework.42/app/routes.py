from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Oleksa'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': ']r;flrplfrlfl'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'rpforkfroikf'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


