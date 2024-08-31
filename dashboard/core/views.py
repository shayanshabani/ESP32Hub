import json

from django.http import JsonResponse
from django.views.generic import TemplateView

from core.models import Device, Sensor, BooleanActuator, IntegerActuator
from core.mqtt_client import SingletonClient


class HomePageView(TemplateView):
    template_name = 'core/index.html'


def get_data(request, uid):
    sensor: Sensor = Sensor.objects.get(uid=uid)
    data = sensor.get_data()
    formated_data = [{'x': d.received_at.timestamp() * 1000, 'y': float(d.message)}
                     for d in data]
    return JsonResponse(formated_data, safe=False)


def get_device_list(request):
    devices = Device.objects.all()
    formatted = []
    for dev in devices:
        formatted.append([str(dev.name), str(dev.token), dev.device_type])
    return JsonResponse(formatted, safe=False)


def turn_on(request, uid):
    device: BooleanActuator = BooleanActuator.objects.get(uid=uid)
    device.turn_on()


def turn_off(request, uid):
    device: BooleanActuator = BooleanActuator.objects.get(uid=uid)
    device.turn_off()


def integer(request, uid):
    data = json.loads(request.body)
    num = data.get('number')
    device: IntegerActuator = IntegerActuator.objects.get(uid=uid)
    device.send_int(num)


def start(request):
    client = SingletonClient().client
    from core.models import Device
    devices = Device.objects.all()
    for device in devices:
        client.subscribe(device.topic, 0)
