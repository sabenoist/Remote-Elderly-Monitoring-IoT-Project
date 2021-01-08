from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
CORS(app)

name = ''
gender = ''
age = 0
resting_heart_rate = 0
cholestrol = 0
fasting_blood_sugar = 0
maximum_heart_rate = 0
body_temperature = 0
blood_pressure = 0
emergency = 0


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/')
def user():
    return render_template('user.html')


@app.route('/alert/')
def alert():
    return render_template('alert.html')


@app.route('/data/resting_heart_rate/', methods=['GET'])
def get_resting_heart_rate():
    return jsonify(resting_heart_rate)


@app.route('/data/cholestrol/', methods=['GET'])
def get_cholestrol():
    return jsonify(cholestrol)


@app.route('/data/fasting_blood_sugar/', methods=['GET'])
def get_fasting_blood_sugar():
    return jsonify(fasting_blood_sugar)


@app.route('/data/maximum_heart_rate/', methods=['GET'])
def get_maximum_heart_rate():
    return jsonify(maximum_heart_rate)


@app.route('/data/body_temperature/', methods=['GET'])
def get_body_temperature():
    return jsonify(body_temperature)


@app.route('/data/blood_pressure/', methods=['GET'])
def get_blood_pressure():
    return jsonify(blood_pressure)


@app.route('/data/emergency/', methods=['GET'])
def get_emergency():
    return jsonify(emergency)


@app.route('/data/name/', methods=['GET'])
def get_name():
    return jsonify(name)


@app.route('/data/gender/', methods=['GET'])
def get_gender():
    return jsonify(gender)


@app.route('/data/age/', methods=['GET'])
def get_age():
    return jsonify(age)


@app.route('/data/', methods=['POST'])
def add_message():
    content = request.json
    loaded_json = json.loads(content)

    global resting_heart_rate
    resting_heart_rate = loaded_json["data"][0][0]
    global cholestrol
    cholestrol = loaded_json["data"][0][1]
    global fasting_blood_sugar
    fasting_blood_sugar = loaded_json["data"][0][2]
    global maximum_heart_rate
    maximum_heart_rate = loaded_json["data"][0][3]
    global body_temperature
    body_temperature = loaded_json["data"][0][4]
    global blood_pressure
    blood_pressure = loaded_json["data"][0][5]
    global emergency
    emergency = loaded_json["data"][0][6]
    global name
    name = loaded_json["data"][0][7]
    global gender
    gender = loaded_json["data"][0][8]
    global age
    age = loaded_json["data"][0][9]
    
    return ('Ok', 200)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

