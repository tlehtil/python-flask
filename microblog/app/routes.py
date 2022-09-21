from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Teemu'}
    posts = [
        {
            'author': {'username':'Väyrysen viskipullo'},
            'body': 'Aina on hyvä syy röypätä'
        },
        {
            'author': {'username':'Pelkuri'},
            'body': 'Maksan velat'
        }
    ]
    return render_template('index.html', title="Pullo", user=user, posts=posts)
