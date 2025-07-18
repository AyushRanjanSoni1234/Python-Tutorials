from flask import Flask, jsonify, request, render_template, redirect, url_for

app = Flask(__name__)

img_path = "ChatGPT Image May 21, 2025, 05_45_39 PM.png"

@app.route('/')
def home():
    return render_template('ets.html')

@app.route('/ets', methods=['GET'])
def get_ets():
    return render_template('ets.html')

if __name__ == '__main__':
    app.run(debug=True)