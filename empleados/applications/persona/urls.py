from django.contrib import admin
from django.urls import path

def DesdeApps(self):
    print('========================Desde app Persona=====================')

urlpatterns = [
    path('persona/',DesdeApps),
]
