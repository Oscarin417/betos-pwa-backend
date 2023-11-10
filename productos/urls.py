from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("contacto/", views.contactos, name='contacto'),
    path("contacto/create/", views.create_contacto, name='create_contacto'),
    path("contacto/edit/<int:c_id>/", views.edit_contacto, name='edit_contacto'),
    path("contacto/delete/<int:c_id>/", views.delete_contacto, name='delete_contacto'),
    path("registro/", views.registro, name='registro'),
    path("productos/", views.productos, name='productos'),
    path("productos/create/", views.create_productos, name='create_productos'),
    path("productos/edit/<int:p_id>/", views.edit_productos, name='edit_productos' ),
    path("productos/delete/<int:p_id>/", views.delete_productos, name='delete_productos'),
    path("usuarios/", views.usuarios, name='usuarios'),
    path("logout/", views.cerrar_sesion, name='logout'),
    path("login/", views.crear_sesion, name='login')
]
