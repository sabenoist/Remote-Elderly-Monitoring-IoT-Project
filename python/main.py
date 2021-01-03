# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/')
def user():
    return render_template('user.html')

@app.route('/alert/')
def alert():
    return render_template('alert.html')
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


