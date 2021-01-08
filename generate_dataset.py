from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
import sys
import paho.mqtt.client as paho
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import random


broker = "127.0.0.1"
broker_port = 1883
client = paho.Client("local")
topic = "sensor_001"

columns = ['age', 'sex', 'resting heart rate', 'cholestrol', 'fasting blood sugar > 120 mg/dl', 'maximum heart rate achieved', 'num']
df = pd.DataFrame(columns=columns)
message_counter = 0


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
    global message_counter
    message_counter += 1
    print (message_counter)
    frame = parse_msg(str(message.payload.decode("utf-8")))[0:4]

    age = random.randint(50,70)
    gender = random.randint(0,1)

    frame = [age, gender] + frame + [1]

    global df
    df.loc[len(df)] = frame

    if message_counter >= 400:
        df.to_csv (r'C:\Users\Sander\Desktop\SU_Internet_Of_Things\heartattack.csv', index=False, header=True)
        sys.exit()


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


if __name__ == '__main__':
    while(not connect_to_mqtt()): # connect to mqtt broker
        print("Error: could not connect to the MQTT broker at " + broker + ":" + str(broker_port) + ". Make sure that the MQTT broker is running!\nRetrying in 5 seconds.")
        time.sleep(5)
    
    client.loop_forever()


