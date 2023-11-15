from django.urls import path
from . import views

urlpatterns = [
    path('', views.productos, name='productos'),
    path("create/", views.create_productos, name='create_productos'),
    path('edit/<int:p_id>/', views.edit_producto, name='edit_productos'),
    path('delete/<int:p_id>/', views.delete_producto, name='delete_productos'),
]