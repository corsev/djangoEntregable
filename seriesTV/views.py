from django.shortcuts import render, redirect

# Create your views here.
from seriesTV.models import Serie


def mostrar_inicio(request):
    lista_series = Serie.objects.all()
    return render(request, 'index.html', {'series': lista_series})

def crear_serie(request):
    if request.method == 'GET':
        return render(request, 'crear_serie.html')
    else:
        serie_nueva = Serie()
        serie_nueva.nombre = request.POST.get ('nombre')
        serie_nueva.genero = request.POST.get ('genero')
        serie_nueva.plataforma = request.POST.get('plataforma')
        serie_nueva.capitulos = request.POST.get('capitulos')
        serie_nueva.anio = request.POST.get('anio')
        Serie.save(serie_nueva)
        return redirect("/seriesTV")
def borrar_serie(request):
    if request.method == 'GET':
        return render(request, 'borrar_serie.html')
    else:
        serie_vieja = Serie()
        serie_vieja.nombre = request.POST.get('nombre')
        Serie.delete(serie_vieja)
        return redirect("/seriesTV")