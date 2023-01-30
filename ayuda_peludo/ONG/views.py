from django.shortcuts import render, redirect
from .models import Tb_Articulo, tb_Mascota
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http.response import HttpResponse

# Create your views here.
@login_required


def home(request):
      return render(request, "home.html")

def mascotas(request):
    mascotalist=tb_Mascota.objects.all()
    return render(request, "gestionMascotas.html",{"lista_mascota":mascotalist})

def contacto(request):
    
    return render(request, "contacto.html")

def consumoApi(request):
    return render(request, "api.html" )  

# def home(request):
#     articuloListados = Tb_Articulo.objects.all()
#     messages.success(request, '¡Articulos Listados!')
#     return render(request, "gestionArticulos.html", {"articulos": articuloListados})

def Add_Articulo(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    stock = request.POST['numStock']
    articulo = Tb_Articulo.objects.create(
        codigo=codigo, nombre=nombre, stock=stock)
    messages.success(request, '¡Artículo Registrado!')
    return redirect('/')

def Edit_Articulo(request):
     codigo = request.POST['txtCodigo']
     nombre = request.POST['txtNombre']
     stock = request.POST['numStock']
     articulo = Tb_Articulo.objects.get(codigo=codigo)
     articulo.nombre = nombre
     articulo.creditos = stock
     articulo.save()
     messages.success(request, '¡Artículo Actualizado!')
     return redirect('/')
def Del_Articulo(request, codigo):
     articulo = Tb_Articulo.objects.get(codigo=codigo)
     articulo.delete()
     messages.success(request, '¡Artículo Eliminado!')
     return redirect('/')

def Edicion_Articulo(request, codigo):
    articulo = Tb_Articulo.objects.get(codigo=codigo)
    return render(request, "edicionArticulo.html", {"articulo": articulo})

def registrarMascota(request):
    codigo=request.POST['txtCodigo']    
    nombre=request.POST['txtNombre'] 
    edad=request.POST['numEdad'] 
    raza=request.POST['txtRaza'] 

    Mascota = tb_Mascota.objects.create(codigo=codigo,  nombre=nombre, edad=edad, raza=raza)
    return redirect('mascota')
    # return render(request, "mascotas.html")


def edicionMascota(request, codigo):
    mascota = tb_Mascota.objects.get(codigo=codigo)
    
    return render(request, "edicionMascota.html", {"mascota":mascota})
    

def editarMascota(request,codigo ):
    codigo=request.POST['txtCodigo']    
    nombre=request.POST['txtNombre'] 
    edad=request.POST['numEdad'] 
    raza=request.POST['txtRaza'] 

    mascota = tb_Mascota.objects.get(codigo=codigo )
    mascota.nombre = nombre
    mascota.edad = edad
    mascota.raza = raza
    mascota.save()
    # return redirect('/')
    # return redirect('/')
    return render(request, "edicionMascota.html", {"mascota":mascota})
    
   
    
    





def eliminacionMascota(request, codigo):
    mascota = tb_Mascota.objects.get(codigo=codigo)
    mascota.delete()
    # return render(request, "gestionMascota.html")
    # return redirect('/')
    # return render(request, "gestionMascotas.html")
    return redirect('mascota')

def logout_request(request):
    logout(request)
    messages.info(request,"saliste de session")
    return redirect('/')



