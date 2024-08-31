from django.shortcuts import render
from django.views.generic import TemplateView

from django.http import HttpResponse
import paho.mqtt.client as mqtt


class HomePageView(TemplateView):
    template_name = 'core/index.html'

def get_data(request):
    now = datetime.now()
    data = [{'x': (now + timedelta(seconds=i)).timestamp() * 1000, 'y': random.randint(10, 90)}
            for i in range(60)]
    return JsonResponse(data, safe=False)
