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

def modificar_serie(request,id):
    if request.method == 'GET':
        modificar_serie = Serie.objects.get(id=id)
        return render(request, 'modificar_serie.html', {"serie":modificar_serie})
    else:
        modificar_serie = Serie.objects.get(id=id)
        modificar_serie.nombre = request.POST.get ('nombre')
        modificar_serie.genero = request.POST.get ('genero')
        modificar_serie.plataforma = request.POST.get('plataforma')
        modificar_serie.capitulos = request.POST.get('capitulos')
        modificar_serie.anio = request.POST.get('anio')
        Serie.save(modificar_serie)
        return redirect("/seriesTV")
def borrar_serie(request):
    if request.method == 'GET':
        return render(request, 'borrar_serie.html')
    else:
        serie_vieja = Serie()
        serie_vieja.id = request.POST.get('id')
        Serie.delete(serie_vieja)
        return redirect("/seriesTV")

def ver_serie(request, id):
    if request.method == 'GET':
        ver_serie = Serie.objects.get(id=id)
        return render(request, 'ver_serie.html', {"serie":ver_serie})
    else:
        ver_serie = Serie.objects.get(id=id)
        ver_serie.nombre = request.POST.get ('nombre')
        ver_serie.genero = request.POST.get ('genero')
        ver_serie.plataforma = request.POST.get('plataforma')
        ver_serie.capitulos = request.POST.get('capitulos')
        ver_serie.anio = request.POST.get('anio')
        return redirect("/seriesTV")

