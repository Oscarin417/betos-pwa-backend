from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from .forms import * 
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
<<<<<<< HEAD
import os
=======
>>>>>>> b1eb03d7aa2737231177b545073b6893f970fb3a

# Create your views here.
def productos(request):
    productos_list = Productos.objects.all()
    items_por_pagina = 5
    paginator = Paginator(productos_list, items_por_pagina)
    page = request.GET.get('page')
    try:
        productos = paginator.page(page)
    except PageNotAnInteger:
        productos = paginator.page(1)
    except EmptyPage:
        productos = paginator.page(paginator.num_pages)
<<<<<<< HEAD
    return render(request, 'productos.html', {'productos': productos})

def create_productos(request):
    if request.method == 'GET':
        return render(request, 'create_productos.html', {
=======
    return render(request, 'productos.html', {
        'productos': productos,
    })

def edit_productos(request, p_id):
    if request.method == 'GET':
        producto = get_object_or_404(Productos, pk=p_id)
        form = ProductoForm(instance=producto)
        return render(request, 'edit_producto.html', {
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
                return render(request, 'edit_producto.html', {
                    'producto': producto,
                    'form': form,
                    'error': 'No se ha podido editar el producto'
                })
            else:
                form.save()
                return redirect('productos')


def create_productos(request):
    if request.method == 'GET':
        return render(request, 'create_producto.html', {
>>>>>>> b1eb03d7aa2737231177b545073b6893f970fb3a
            'form': ProductoForm
        })
    else:
        try:
            form = ProductoForm(request.POST, request.FILES)
            form.save()
            return redirect('productos')
        except ValueError:
<<<<<<< HEAD
            return render(request, 'create_productos.html', {
=======
            return render(request, 'create_producto.html', {
>>>>>>> b1eb03d7aa2737231177b545073b6893f970fb3a
                'form': form,
                'error': 'Ingresa datos validos'
            })

<<<<<<< HEAD
def delete_producto(request, p_id):
    producto = get_object_or_404(Productos, pk=p_id)
    imagen_path = producto.imagen.path
    if request.method == 'POST':
        producto.delete()
        if os.path.exists(imagen_path):
            os.remove(imagen_path)
        return redirect('productos')

def edit_producto(request, p_id):
    if request.method == 'GET':
        producto = get_object_or_404(Productos, pk=p_id)
        form = ProductoForm(instance=producto)
        return render(request, 'edit_productos.html', {
            'producto': producto,
            'form': form
        })
    else:
        try:
            producto = get_object_or_404(Productos, pk=p_id)
            form = ProductoForm(request.POST, request.FILES, instance=producto)
            form.save()
            return redirect('productos')
        except ValueError:
            producto = get_object_or_404(Productos, pk=p_id)
            form = ProductoForm(request.POST, request.FILES, instance=producto)
            return render(request, 'edit_productos.html', {
                'producto': producto,
                'form': form,
                'error': 'Ingresa datos válidos'
            })
=======
def delete_productos(request, p_id):
    producto = get_object_or_404(Productos, pk=p_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('productos')
>>>>>>> b1eb03d7aa2737231177b545073b6893f970fb3a
