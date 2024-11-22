from django.urls import path
from .views import entregable_view, acceso, lista_entregables

urlpatterns = [
    path('entregable.html', entregable_view, name='entregable'),
    path('acceso.html', acceso, name='acceso'),
    path('lista_entregables.html', lista_entregables, name='lista_entregables'),
]
