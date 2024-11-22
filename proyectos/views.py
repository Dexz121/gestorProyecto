from django.shortcuts import render, redirect
from .forms import EntregableForm
from .models import Entregable
from django.core.serializers import serialize
from django.http import JsonResponse

def entregable_view(request):
    return render(request, 'proyectos/entregable.html')

def acceso(request):
    return render(request, 'proyectos/acceso.html')

def lista_entregables(request):
  entregables = Entregable.objects.all()  # Replace with your query logic
  context = {'entregables': entregables}
  return render(request, 'proyectos/lista_entregables.html', context)

def about_page_view(request):
    return render(request, "proyectos/about.html")

def crear_entregable(request):
    if request.method == 'POST':
        form = EntregableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/proyectos/lista_entregables/')  # Cambia a la ruta que desees
    else:
        form = EntregableForm()
    return render(request, 'proyectos/entregable.html', {'form': form})