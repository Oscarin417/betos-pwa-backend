from django.urls import path
from . import views

urlpatterns = [
    path('', views.contacto, name='contactos'),
    path("create/", views.create_contacto, name='create_contactos'),
    path('edit/<int:c_id>/', views.edit_contacto, name='edit_contactos'),
    path('delete/<int:c_id>/', views.delete_contacto, name='delete_contactos')
]