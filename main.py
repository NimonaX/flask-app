from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return 'hello vishal'

@app.route('/index')
def index():
    return "this is index page"
if __name__ == '__main__':
    app.run(debug=True)

# $env:FLASK_APP = "flaskblog.py" 
#  $env:FLASK_DEBUG = 1 