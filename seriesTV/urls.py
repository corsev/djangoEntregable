
from django.contrib import admin
from django.urls import path
from .views import *




urlpatterns = [
    path('', mostrar_inicio),
    path('seriesTV/crear_serie', crear_serie),
    path('seriesTV/borrar_serie/<id>', borrar_serie),
    path('seriesTV/ver_serie/<id>', ver_serie),
    path('seriesTV/modificar_serie/<id>', modificar_serie)


]