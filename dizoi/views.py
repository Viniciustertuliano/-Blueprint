from flask import Blueprint, render_template

dizoi = Blueprint('dizoi', __name__, url_prefix='/ola', template_folder='templates')

@dizoi.route('/')
def ola():
    return render_template('ola.html')

@dizoi.route('/tchau')
def tchau():
    return '<h1>TCHAU!</h1>'