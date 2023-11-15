<<<<<<< HEAD
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'contacto', views.Contacto, 'contacto')
=======
from django.urls import path
from . import views
>>>>>>> b1eb03d7aa2737231177b545073b6893f970fb3a

urlpatterns = [
    path('', views.contacto, name='contactos'),
    path("create/", views.create_contacto, name='create_contactos'),
    path('edit/<int:c_id>/', views.edit_contacto, name='edit_contactos'),
<<<<<<< HEAD
    path('delete/<int:c_id>/', views.delete_contacto, name='delete_contactos'),
    path('api/', include(router.urls))
=======
    path('delete/<int:c_id>/', views.delete_contacto, name='delete_contactos')
>>>>>>> b1eb03d7aa2737231177b545073b6893f970fb3a
]