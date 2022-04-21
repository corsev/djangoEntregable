from django.db import models
from django.urls import reverse

class Serie(models.Model):
     nombre = models.TextField(max_length=200)
     genero = models.TextField(max_length=1000)
     plataforma = models.TextField(max_length=200)
     capitulos = models.IntegerField(default=0)
     anio = models.IntegerField(default=1970)

     def __str__(self):
          return self.nombre
