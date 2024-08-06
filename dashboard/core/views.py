from django.shortcuts import render
from django.views.generic import TemplateView

from django.http import HttpResponse
import paho.mqtt.client as mqtt


class HomePageView(TemplateView):
    template_name = 'core/index.html'


MQTT_BROKER = "192.168.136.198"
MQTT_PORT = 1883
MQTT_KEEPALIVE = 60
MQTT_TOPIC_BUZZER = "buzzer"
MQTT_TOPIC_LED = "led"
MQTT_TOPIC_SERVO = "servo"
MQTT_USER = "uname"
MQTT_PASSWORD = "upass"


def buzzer_on(request):
    client = mqtt.Client()
    client.username_pw_set(MQTT_USER, MQTT_PASSWORD)
    client.connect(MQTT_BROKER, MQTT_PORT, MQTT_KEEPALIVE)

    client.publish(MQTT_TOPIC_BUZZER, "on")
    client.disconnect()

    return HttpResponse("Buzzer turned on", status=200)


def led_on(request):
    client = mqtt.Client()
    client.username_pw_set(MQTT_USER, MQTT_PASSWORD)
    client.connect(MQTT_BROKER, MQTT_PORT, MQTT_KEEPALIVE)

    client.publish(MQTT_TOPIC_LED, "on")
    client.disconnect()

    return HttpResponse("LED turned on", status=200)


def buzzer_off(request):
    client = mqtt.Client()
    client.username_pw_set(MQTT_USER, MQTT_PASSWORD)
    client.connect(MQTT_BROKER, MQTT_PORT, MQTT_KEEPALIVE)

    client.publish(MQTT_TOPIC_BUZZER, "off")
    client.disconnect()

    return HttpResponse("Buzzer turned off", status=200)


def led_off(request):
    client = mqtt.Client()
    client.username_pw_set(MQTT_USER, MQTT_PASSWORD)
    client.connect(MQTT_BROKER, MQTT_PORT, MQTT_KEEPALIVE)

    client.publish(MQTT_TOPIC_LED, "off")
    client.disconnect()

    return HttpResponse("LED turned off", status=200)


def servo(request, pk):
    client = mqtt.Client()
    client.username_pw_set(MQTT_USER, MQTT_PASSWORD)
    client.connect(MQTT_BROKER, MQTT_PORT, MQTT_KEEPALIVE)

    client.publish(MQTT_TOPIC_SERVO, str(pk))
    client.disconnect()

    return HttpResponse(f"Servo position set to {pk}", status=200)
