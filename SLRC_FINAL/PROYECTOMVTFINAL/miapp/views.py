from django.shortcuts import render

# Create your views here.

def Index(request):

    return render(request,"index.html",{}) 
    
def Cursos(request):
    mensaje="Listado de Cursos"
    return render(request,"cursos.html",{"mensaje":mensaje}) 

def Crearcursos(request):
    mensaje="Agregar Curso"
    return render(request,"crearCursos.html",{"mensaje":mensaje}) 

def Carreras(request):
    mensaje="Listado de Carreras"
    return render(request,"carreras.html",{"mensaje":mensaje}) 

def Crearcarreras(request):
    mensaje="Agregar Carreras"
    return render(request,"crearCarreras.html",{"mensaje":mensaje}) 