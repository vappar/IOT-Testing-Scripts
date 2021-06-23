import paho.mqtt.client as paho  # mqtt library
import os
import json
import time
from datetime import datetime

ACCESS_TOKEN = 'mgPSV5pE03klR26QnQ4Y'  # Token of your device
broker = "localhost"  # host name
port = 1883  # data listening port


def on_publish(client, userdata, result):  # create function for callback
    print("data published to thingsboard \n")
    pass



client1 = paho.Client("control1")  # create client object
client1.on_publish = on_publish  # assign function to callback
client1.username_pw_set(ACCESS_TOKEN)  # access token from thingsboard device
client1.connect(broker, port, keepalive=60)  # establish connection

client1.loop_start()


while True:
    payload = "{"
    payload += "\"Humidity\":61,";
    payload += "\"Temperature\":22";
    payload += "}"
    ret = client1.publish("v1/devices/me/telemetry", payload)  # topic-v1/devices/me/telemetry
    print("Please check LATEST TELEMETRY field of your device")
    print(payload);
    time.sleep(5)

client1.loop_stop()
client1.disconnect()
