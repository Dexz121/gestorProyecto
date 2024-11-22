from django.contrib import admin
from django.urls import path, include
from proyectos.views import acceso 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', acceso, name='inicio'),
    path('acceso/', acceso, name='acceso'),
    path('proyectos/', include('proyectos.urls')), 
]
