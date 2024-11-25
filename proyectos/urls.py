from django.urls import path
from .views import (
    entregable_view,
    saveNewEntregable, 
    acceso, 
    lista_entregables, 
    about_page_view, 
    crear_entregable,
    actualizar_entregable)

urlpatterns = [
    path('entregable/<int:id>/', entregable_view, name='detalle_entregable'),
    path('entregable/', saveNewEntregable, name='saveNewEntregable'),
    path('acceso/', acceso, name='acceso'),
    path('lista_entregables/', lista_entregables, name='lista_entregables'),
    path('about/', about_page_view, name='about'),
    path('crear_entregable/', crear_entregable, name='crear_entregable'),
    path('entregable/actualizar/<int:id>/', actualizar_entregable, name='actualizar_entregable'),
]
