from flask import Flask
"""
It creates a instance of the Flask class which 
will be your WSGI(web server gateway interface) application.
"""

## WSGI Application
app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to the Flask App! This is the home page. How can I assist you today?"

@app.route('/index')
def index():
    return "This is the index page. You can find various resources here."


if __name__ == '__main__':
    app.run(debug=True)