import json

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from core.models import Device, Sensor, BooleanActuator, IntegerActuator
from core.mqtt_client import SingletonClient


class HomePageView(TemplateView):
    template_name = 'core/index.html'


def get_data(request, uid):
    sensor: Sensor = Sensor.objects.get(token=uid)
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
    device: BooleanActuator = BooleanActuator.objects.get(token=uid)
    device.turn_on()
    return JsonResponse(data={'data': 'success'})


def turn_off(request, uid):
    device: BooleanActuator = BooleanActuator.objects.get(token=uid)
    device.turn_off()
    return JsonResponse(data={'data': 'success'})


def integer(request, uid):
    num = request.GET.get('value',None)
    device: IntegerActuator = IntegerActuator.objects.get(token=uid)
    device.send_int(num)
    return JsonResponse(data={'data': 'success'})


def start(request):
    client = SingletonClient().client
    from core.models import Device
    devices = Device.objects.all()
    for device in devices:
        client.subscribe(device.topic, 0)
    return JsonResponse(data={'data': 'success'})


def add(request):
    name = request.GET.get('name')
    device_type = request.GET.get('type')
    from core.models import Sensor, BooleanActuator, IntegerActuator
    if int(device_type) == 0:
        BooleanActuator.objects.create(name=name, topic=name, device_type=device_type)
    elif int(device_type) == 1:
        IntegerActuator.objects.create(name=name, topic=name, device_type=device_type)
    else:
        Sensor.objects.create(name=name, topic=name, device_type=device_type)
    return JsonResponse(data={'data': 'success'})


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'})
        else:
            return JsonResponse({'message': 'Invalid credentials'}, status=400)

@csrf_exempt
def signup_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        if User.objects.filter(username=username).exists():
            return JsonResponse({'message': 'User already exists'}, status=400)
        user = User.objects.create_user(username=username, password=password)
        return JsonResponse({'message': 'Signup successful'})