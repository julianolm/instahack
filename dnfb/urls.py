from django.urls import path
from .views import home, dnfb


app_name = 'dnfb'
urlpatterns = [
    path('', home, name='home'),
    path('dnfb/', dnfb, name='dnfb'),
]