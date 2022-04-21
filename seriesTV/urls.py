
from django.contrib import admin
from django.urls import path
from .views import *




urlpatterns = [
    path('', mostrar_inicio),
    path('seriesTV/crear_serie', crear_serie),
    path('seriesTV/borrar_serie', borrar_serie)

]