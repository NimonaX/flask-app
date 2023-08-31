from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return 'hello vishal'

if __name__ == '__main__':
    app.run(debug=True)

# $env:FLASK_APP = "flaskblog.py" 
#  $env:FLASK_DEBUG = 1 