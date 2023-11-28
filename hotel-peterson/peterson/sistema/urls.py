from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('reserva/', views.reserva, name='reserva'),
    path('login/', views.login, name='login'),
    path('registro/', views.registro, name='registro'),
    path('pago/', views.pago, name='pago')
]