"""PROYECTOMVTFINAL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from miapp import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.Index),
    path('cursos/',views.Cursos, name='listarcurso'),
    path('crearCursos/',views.Crearcursos, name='Crearcurso'),
    path('save_cursos/',views.save_cursos, name='save_cursos'),
    path('eliminarcurso/<int:id>',views.eliminar_curso, name='eliminarcurso'),
    path('carreras/',views.Carreras),
    path('crearCarreras',views.Crearcarreras),
]
