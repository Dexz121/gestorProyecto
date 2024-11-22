from django.urls import path
from .views import entregable_view, acceso, lista_entregables, about_page_view, crear_entregable

urlpatterns = [
    path('entregable/', entregable_view, name='entregable'),
    path('acceso/', acceso, name='acceso'),
    path('lista_entregables/', lista_entregables, name='lista_entregables'),
    path('about/', about_page_view, name='about'),
    path('entregable/', crear_entregable, name='crear_entregable'),
]
