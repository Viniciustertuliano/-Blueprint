from flask import Flask,  render_template

app = Flask('hello_blueprint')

@app.route('/')
def index():
    return render_template('index.html')

from dizoi.views import dizoi
app.register_blueprint(dizoi)