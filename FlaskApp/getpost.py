from flask import Flask, render_template, request

app = Flask(__name__) #WSGI application

@app.route('/')
def welcome():
    return "Welcome to the home page"

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    # if request.method == 'POST':
    #     name = request.form['name']
    #     email = request.form['email']
    #     return f"Name: {name}, Email: {email}"
    return render_template('form.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        return f"Name: {name}, Email: {email}"
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)