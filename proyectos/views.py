from django.shortcuts import render

def entregable_view(request):
    return render(request, 'proyectos/entregable.html')

def acceso(request):
    return render(request, 'proyectos/acceso.html')

def lista_entregables(request):
    return render(request, 'proyectos/lista_entregables.html')