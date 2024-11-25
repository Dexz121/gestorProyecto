from django.shortcuts import render, redirect, get_object_or_404
from .forms import EntregableForm
from .models import Entregable
from django.core.serializers import serialize
from django.http import JsonResponse

def entregable_view(request, id):
    try:
        entregable = Entregable.objects.get(id=id)
        print(f"Entregable encontrado: {entregable}")
    except Entregable.DoesNotExist:
        print(f"El entregable con ID {id} no existe.")
        return render(request, '404.html')  # O usa un template de error personalizado
    return render(request, 'proyectos/entregable.html', {'entregable': entregable})

def saveNewEntregable(request):
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

def actualizar_entregable(request, id):
    if request.method == "POST":
        entregable = get_object_or_404(Entregable, id=id)

        # Obtén los datos del formulario
        asunto = request.POST.get("asunto", "")
        estado = request.POST.get("estado", "")
        horas_estimadas = request.POST.get("horas_estimadas", "0")
        fecha_inicio = request.POST.get("fecha_inicio", "")
        fecha_finalizacion = request.POST.get("fecha_finalizacion", "")
        descripcion = request.POST.get("descripcion", "")
        comentarios = request.POST.get("comentarios", "")
        persona_asignada = request.POST.get("persona_asignada", "0")

        # Validar y asignar campos
        entregable.asunto = asunto
        entregable.estado = estado
        entregable.horas_estimadas = int(horas_estimadas) if horas_estimadas else 0
        entregable.fecha_inicio = fecha_inicio if fecha_inicio else None  # Valida fechas
        entregable.fecha_finalizacion = fecha_finalizacion if fecha_finalizacion else None
        entregable.descripcion = descripcion
        entregable.comentarios = comentarios
        entregable.persona_asignada = int(persona_asignada) if persona_asignada else None

        # Guarda los cambios
        entregable.save()

        return JsonResponse({"success": True, "message": "Entregable actualizado correctamente."})
    return JsonResponse({"success": False, "message": "Método no permitido."})