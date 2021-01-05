import pandas as pd
import paho.mqtt.client as paho
import time
import requests # this is new -- used in 'send_to_webclient'

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

name = "John"
age = 63
sex = 1 # male

def on_log(client, userdata, level, buff):  # mqtt logs function
    print(buff)

def on_connect(client, userdata, flags, rc):  # connect to mqtt broker function
    if rc == 0:
        client.connected_flag = True  # set flags
        print("Connected Info")
    else:
        print("Bad connection returned code = " + str(rc))
        client.loop_stop()

def on_disconnect(client, userdata, rc):  # disconnect to mqtt broker function
    print("Client disconnected OK")

def on_publish(client, userdata, mid):  # publish to mqtt broker
    print("In on_pub callback mid=" + str(mid))

def on_subscribe(client, userdata, mid, granted_qos):  # subscribe to mqtt broker
    print("Subscribed", userdata)

def on_message(client, userdata, message):  # get message from mqtt broker
    # print("New message received: ", str(message.payload.decode("utf-8")), "Topic : %s ", message.topic, "Retained : %s", message.retain)
    frame = parse_msg(str(message.payload.decode("utf-8")))

    if (heart_attack(frame[0:4]) or possible_emergency(frame[4:])):
    	frame.append(1) # emergency
    else:
    	frame.append(0) # no emergency

    frame_msg = pd.DataFrame(data=[frame], columns=["resting heart rate", "cholestrol", "fasting blood sugar", "maximum heart rate", "body temperature", "bloodpressure", "emergency"])

    send_to_webclient(frame_msg)

def connectToMqtt():  # connect to MQTT broker main function
    print("Connecting to MQTT broker")
    # client.username_pw_set(username="", password="")
    client.on_log = on_log
    client.on_connect = on_connect
    client.on_publish = on_publish
    client.on_subscribe = on_subscribe

    client.connect(broker, broker_port, keepalive=600)
    ret = client.subscribe(topic, qos=0)
    print("Subscribed return = " + str(ret))
    client.on_message = on_message

def parse_msg(msg):
	data_dict = {}
	msg = msg.split(";")

	for data in msg:
		data = data.strip().split(",")
		data_dict[data[0]] = float(data[1])

	frame = [data_dict["resting heart rate"], data_dict["cholestrol"], data_dict["fasting blood sugar"], data_dict["maximum heart rate"], data_dict["body temperature"], data_dict["bloodpressure"]]

	return frame

def heart_attack(frame):
	return False

def possible_emergency(frame):
	if frame[0] < undercooling or frame[0] > dangerous_fever:
		return True
	elif frame[1] < low_blood_pressure or frame[1] > high_blood_pressure:
		return True
	else:
		return False

def send_to_webclient(frame):
    data_json = frame.to_json(orient = "split") # making dataframe to json

    url = "http://" + webserver + ":" + str(webserver_port) + webserver_route + name # url to the server here 
    print(url)
    try:
        r = requests.post(url, json = data_json) # could replace 'json' with 'data'. for more info: https://www.w3schools.com/python/ref_requests_post.asp
        print("Flask webserver: " + str(r))
    except Exception as e:
        print("Flask related exception: " + str(e))


connectToMqtt()  # connect to mqtt broker
client.loop_forever()
