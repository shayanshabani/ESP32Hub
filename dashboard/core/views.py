import json

from django.http import JsonResponse
from django.views.generic import TemplateView

from core.models import Device, Sensor, BooleanActuator, IntegerActuator


class HomePageView(TemplateView):
    template_name = 'core/index.html'


def get_data(request, uid):
    sensor: Sensor = Device.objects.get(uid=uid)
    data = sensor.get()
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
    device: BooleanActuator = Device.objects.get(uid=uid)
    device.turn_on()


def turn_off(request, uid):
    device: BooleanActuator = Device.objects.get(uid=uid)
    device.turn_off()


def integer(request, uid):
    data = json.loads(request.body)
    num = data.get('number')
    device: IntegerActuator = Device.objects.get(uid=uid)
    device.send_int(num)
