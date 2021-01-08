from sklearn.naive_bayes import GaussianNB
import pandas as pd
import paho.mqtt.client as paho
import time
import requests
import pickle 
import sys

broker = "127.0.0.1"
broker_port = 1883
webserver = "127.0.0.1"
webserver_port = 5000
webserver_route = "/data/"
client = paho.Client("local")
topic = "sensor_001"

dangerous_fever = 41
undercooling = 35
high_blood_pressure = 160
low_blood_pressure = 50

name = "Smith"
age = 63
gender = 0 # male


def on_log(client, userdata, level, buff):
    print(buff)


def on_connect(client, userdata, flags, rc): 
    if rc == 0:
        client.connected_flag = True 
        print("Connected Info")
    else:
        print("Bad connection returned code = " + str(rc))
        client.loop_stop()


def on_disconnect(client, userdata, rc): 
    print("Client disconnected OK")


def on_subscribe(client, userdata, mid, granted_qos): 
    print("Subscribed", userdata)


def on_message(client, userdata, message):  
    frame = parse_msg(str(message.payload.decode("utf-8")))

    if (heart_attack(frame[0:4]) or possible_emergency(frame[4:])):
    	frame.append(1) # emergency
    else:
    	frame.append(0) # no emergency

    frame.append(name)
    frame.append(gender)
    frame.append(age)

    frame_msg = pd.DataFrame(data=[frame], columns=["resting heart rate", "cholestrol", "fasting blood sugar", "maximum heart rate", "body temperature", "bloodpressure", "emergency", "name", "gender", "age"])

    send_to_webclient(frame_msg)


def connect_to_mqtt(): 
    try:
        print("Connecting to MQTT broker")
        client.on_log = on_log
        client.on_connect = on_connect
        client.on_subscribe = on_subscribe

        client.connect(broker, broker_port, keepalive=600)
        ret = client.subscribe(topic, qos=0)
        print("Subscribed return = " + str(ret))
        client.on_message = on_message
        return True
    except Exception as e:
        return False


def parse_msg(msg):
	data_dict = {}
	msg = msg.split(";")

	for data in msg:
		data = data.strip().split(",")
		data_dict[data[0]] = float(data[1])

	frame = [data_dict["resting heart rate"], data_dict["cholestrol"], data_dict["fasting blood sugar"], data_dict["maximum heart rate"], data_dict["body temperature"], data_dict["bloodpressure"]]

	return frame


def heart_attack(frame):
    prediction = classifier.predict([[age] + [gender] + frame])
    return prediction


def possible_emergency(frame):
	if frame[0] < undercooling or frame[0] > dangerous_fever:
		return True
	elif frame[1] < low_blood_pressure or frame[1] > high_blood_pressure:
		return True
	else:
		return False


def send_to_webclient(frame):
    data_json = frame.to_json(orient = "split")

    url = "http://" + webserver + ":" + str(webserver_port) + webserver_route
    try:
        r = requests.post(url, json = data_json) 
        print("Flask webserver: " + str(r))
    except Exception as e:
        print("Flask related exception: " + str(e))


def load_classifier():
    print("Loading classifier from gaussian_bayes_model pickle file")

    try:
        global classifier
        classifier = pickle.load(open("gaussian_bayes_model.pickle", 'rb'))
        print("Finished loading classifier")
    except Exception as e:
        print("Error: could not find or load gaussian_bayes_model pickle file.")
        sys.exit()


if __name__ == '__main__':
    load_classifier()

    while(not connect_to_mqtt()): # connect to mqtt broker
        print("Error: could not connect to the MQTT broker at " + broker + ":" + str(broker_port) + ". Make sure that the MQTT broker is running!\nRetrying in 5 seconds.")
        time.sleep(5)
    
    client.loop_forever()
