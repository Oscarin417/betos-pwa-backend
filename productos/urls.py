from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.productos, name='productos'),
    path("create/", views.create_productos, name='create_productos'),
    path('edit/<int:p_id>/', views.edit_producto, name='edit_productos'),
    path('delete/<int:p_id>/', views.delete_producto, name='delete_productos'),
=======
    path("", views.productos, name='productos'),
    path('create/', views.create_productos, name='create_productos'),
    path('edit/<int:p_id>/', views.edit_productos, name='edit_productos'),
    path('delete/<int:p_id>/', views.delete_productos, name='delete_productos')
>>>>>>> b1eb03d7aa2737231177b545073b6893f970fb3a
]