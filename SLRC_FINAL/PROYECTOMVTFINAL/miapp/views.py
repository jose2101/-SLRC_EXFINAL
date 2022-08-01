from unicodedata import name
from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Course
from django.contrib import messages

# Create your views here.

def Index(request):

    return render(request,"index.html",{}) 
    
def Cursos(request):
    cursos = Course.objects.all()
    return render(request,"cursos.html",{
        'cursos':cursos,
        'titulo':'Listado de Cursos'
     }) 
def save_cursos(request):
    if request.method == 'POST':
                codigo = request.POST['codigo']
                nombre = request.POST['nombre']
                horario = request.POST['horario']
                creditos = request.POST['creditos']
                estado = request.POST['estado']
                curso = Course(
                    code = codigo,
                    name = nombre,
                    hour = horario,
                    credits = creditos,
                    state = estado
                )
                curso.save()
                messages.success(request, f'Se agregó correctamente el curso {curso.name}')
    return redirect('listarcurso')

def Crearcursos(request):
    mensaje="Agregar Curso"
    return render(request,"crearCursos.html",{"mensaje":mensaje}) 

def eliminar_curso(request,id):
    curso = Course.objects.get(pk=id)
    curso.delete()
    return redirect('listarcurso')

def Carreras(request):
    mensaje="Listado de Carreras"
    return render(request,"carreras.html",{"mensaje":mensaje}) 

def Crearcarreras(request):
    mensaje="Agregar Carreras"
    return render(request,"crearCarreras.html",{"mensaje":mensaje}) 