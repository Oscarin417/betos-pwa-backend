from django.urls import path
from . import views

urlpatterns = [
    path("", views.productos, name='productos'),
    path('create/', views.create_productos, name='create_productos'),
    path('edit/<int:p_id>/', views.edit_productos, name='edit_productos'),
    path('delete/<int:p_id>/', views.delete_productos, name='delete_productos')
]