import threading
import time
import redis

import paho.mqtt.client as mqtt
import django
import os

from core.models import DataModel

MQTT_BROKER = "192.168.136.198"
MQTT_PORT = 1883
MQTT_KEEPALIVE = 60
MQTT_TOPICS = [("light", 0), ("sound", 0), ("ultrasound", 0)]
MQTT_USER = "uname"
MQTT_PASSWORD = "upass"
MQTT_DEVICES = {}

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
# django.setup()


def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    for topic, qos in MQTT_TOPICS:
        client.subscribe(topic, qos)


def on_message(client, userdata, msg):
    print(f"Topic: {msg.topic}\nMessage: {msg.payload.decode()}")
    MQTT_DEVICES[msg.topic].on_message(msg.payload.decode())


def start_mqtt_client():
    redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set(MQTT_USER, MQTT_PASSWORD)
    client.connect(MQTT_BROKER, MQTT_PORT, MQTT_KEEPALIVE)
    client.loop_forever()


def run_mqtt_client_in_thread():
    mqtt_thread = threading.Thread(target=start_mqtt_client)
    mqtt_thread.daemon = True
    mqtt_thread.start()
