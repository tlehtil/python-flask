from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Teemu'}
    return render_template('index.html', title="Pullo", user=user)
