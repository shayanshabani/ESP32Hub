from django.urls import path

from core import views
from core.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('buzzer-on/', views.buzzer_on, name='buzzer_on'),
    path('led-on/', views.led_on, name='led_on'),
    path('servo/<int:pk>', views.servo, name='servo'),
    path('buzzer-off/', views.buzzer_off, name='buzzer_off'),
    path('led-off/', views.led_off, name='led_off'),
]
