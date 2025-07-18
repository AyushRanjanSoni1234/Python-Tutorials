from flask import Flask, render_template

# Create an instance of the Flask class (WSGI application)
app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to the Flask App! This is the home page"

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)