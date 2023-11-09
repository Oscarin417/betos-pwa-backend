from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import * 
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def contactos(request):
    contactos = Contactos.objects.all()
    return render(request, 'contacto/contactos.html', {'contactos': contactos})

@login_required
def create_contacto(request):
    if request.method == 'GET':
        return render(request, 'contacto/create_contacto.html', {
            'form': CreateContactoForm
        })
    else:
        try:
            form = CreateContactoForm(request.POST)
            form.save()
            return redirect('contacto')
        except ValueError:
            return render(request, 'contacto/create_contacto.html', {
                'form': CreateContactoForm,
                'error': 'Ingresa datos validos'
            })

@login_required
def delete_contacto(request, c_id):
    contacto = get_object_or_404(Contactos, pk=c_id)
    if request.method == 'POST':
        contacto.delete()
        return redirect('contacto')

@login_required
def edit_contacto(request, c_id): 
    if request.method == 'GET':
        contacto = get_object_or_404(Contactos, pk=c_id)
        form = CreateContactoForm(instance=contacto)
        return render(request, 'contacto/edit_contacto.html', {
            'contacto': contacto,
            'form': form
        })
    else:
        try:
            contacto = get_object_or_404(Contactos, pk=c_id)
            form = CreateContactoForm(request.POST, instance=contacto)
            form.save()
            return redirect('contacto')
        except ValueError:
            contacto = get_object_or_404(Contactos, pk=c_id)
            form = CreateContactoForm(request.POST, instance=contacto)
            return render(request, 'contacto/edit_contacto.html', {
                'contacto': contacto,
                'form': form,
                'error': 'Ingresa datos validos'
            })

def home(request):
    contactos = Contactos.objects.all().count()
    productos = Productos.objects.all().count()
    usuarios = User.objects.all().count()
    return render(request, 'home.html', {
        'contactos': contactos,
        'productos': productos,
        'usuarios': usuarios
    })

def registro(request):
    if request.method == 'GET':
        return render(request, 'registro.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # registrar usuario
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                        password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect("productos")
            except IntegrityError:
                return render(request, 'registro.html', {
                    'form': UserCreationForm,
                    "error": 'El usuario ya existe'
                })
        else:
            return render(request, 'registro.html', {
                'form': UserCreationForm,
                "error": 'Las contraseñas no coinciden'
            })

@login_required
def productos(request):
    productos = Productos.objects.all()
    return render(request, 'producto/productos.html', {'productos' : productos})

def edit_productos(request, p_id):
    if request.method == 'GET':
        producto = get_object_or_404(Productos, pk=p_id)
        form = ProductoForm(instance=producto)
        return render(request, 'producto/edit_producto.html', {
            'form': form,
            'producto': producto
        })
    else:
        try:
            producto = get_object_or_404(Productos, pk=p_id)
            form = ProductoForm(request.POST, request.FILE, instance=producto)
            form.save()
            return redirect('productos')
        except ValueError:
            producto = get_object_or_404(Productos, pk=p_id)
            form = ProductoForm(request.POST, instance=producto)
            if not request.FILES:
                return render(request, 'producto/edit_producto.html', {
                    'producto': producto,
                    'form': form,
                    'error': 'No se ha podido editar el producto'
                })
            else:
                form.save()
                return redirect('productos')


def create_productos(request):
    if request.method == 'GET':
        return render(request, 'producto/create_producto.html', {
            'form': ProductoForm
        })
    else:
        try:
            form = ProductoForm(request.POST, request.FILES)
            form.save()
            return redirect('productos')
        except ValueError:
            return render(request, 'producto/create_producto.html', {
                'form': form,
                'error': 'Ingresa datos validos'
            })

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('home')

def crear_sesion(request):
    if request.method == 'GET':
        return render(request, 'login.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'],
                     password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {
                'form': AuthenticationForm,
                'error': 'El usuario o la contraseña son incorrectas'
            })
        else:
            login(request, user)
            return redirect('home')
