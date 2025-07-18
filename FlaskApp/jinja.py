### Building URL dynamically
### Variable Rule
### Jinja 2 Template Engine
"""
{{ variable }} - to print a variable
{% block %} - to define a block, loop and condition
{# comment #} - to add a comment
"""


from flask import Flask, render_template, request, redirect, url_for

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
    return render_template('form.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        return f"Name: {name}, Email: {email}"
    return render_template('form.html')

# variable rule
@app.route('/success/<int:score>')
def success(score):
    if score >= 50:
        return f"Success! Your score is {score}."
    else:
        return f"Failure! Your score is {score}."

# Jinja 2 Template Engine    
@app.route('/successres/<int:score>')
def successres(score):
    # if score >= 50:
    #     return render_template('success.html', score=score)
    # else:
    #     return render_template('failure.html', score=score) 

    res = ''
    if score >= 50:
        res = 'success'
    else:
        res = 'failure'
    exp = {
        'score': score,
        'result': res
    }
    return render_template('result.html', results=exp)   

# If condition
@app.route('/successressult/<int:score>')
def successressult(score):
    return render_template('result1.html', results=score)  

@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result1.html', results=score)  

# Building URL dynamically
@app.route('/submitx', methods=['GET', 'POST'])
def submitx():
    total_score = 0
    if request.method == 'POST':
        Science = float(request.form['science'])
        Math = float(request.form['maths'])
        English = float(request.form['english'])
        Computer = float(request.form['computer'])
        Hindi = float(request.form['hindi'])
        Sanskrit = float(request.form['sanskrit'])
        total_score = (Science + Math + English + Computer + Hindi + Sanskrit) / 6

    else:
        return render_template('getresult.html')    

    return redirect(url_for('successres', score=total_score))    

if __name__ == '__main__':
    app.run(debug=True, port=5002)