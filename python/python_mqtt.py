import paho.mqtt.client as mqtt
import time

# everything works so far, but the function is not being triggered 

#####
def on_message(client, userdata, message):
    print("message received, ", str(message.payload.decode("utf-8")))
    print("message topic = ", message.topic)
    print("message qos = ", message.qos)
#####

# Choosing address, same as publisher
#broker_address = "mongodb://127.0.0.1:27017/MQTT" #this might need to change
broker_address = "127.0.0.1"
# Create a new instance
print("creating new instance")
client = mqtt.Client("P1")

# Attatching function
print("attatching function")
client.on_message = on_message
# Connect to the broker
print("connect to the broker")
client.connect(broker_address, port=1833)
client.loop_start()

# Subscribe to the topic
print("subscribing to topic")
client.subscribe("sensor_001")

time.sleep(20)#wait

client.loop_stop() #stop the loop
