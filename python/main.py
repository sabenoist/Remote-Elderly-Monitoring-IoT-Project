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


# Yazz added things here that she does not fully understand
# plese read this for more info: https://stackoverflow.com/questions/20001229/how-to-get-posted-json-in-flask
# I used the example in the second answer
@app.route('/api/add_message/', methods=['GET', 'POST'])
def add_message():
    content = request.json # the json should here be put in the content variable
    print (content['mytext']) # this is where things are done with the json - this was just an example
    # return jsonify({"uuid":uuid}) # not sure if this is needed?
    return('', 200)