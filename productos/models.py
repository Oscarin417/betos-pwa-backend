from django.db import models

# Create your models here.
class Productos(models.Model):
<<<<<<< HEAD
    nombre = models.CharField(max_length=100, null=False, blank=False)
    descripcion = models.TextField(null=False, blank=False)
    precio = models.DecimalField(decimal_places=2, max_digits=9, null=False)
    imagen = models.ImageField(upload_to="images/", null=False, blank=False)
=======
    nombre = models.CharField(max_length=100, null=False)
    precio = models.DecimalField(decimal_places=2, max_digits=9, null=False)
    descripcion = models.TextField(null=False)
    imagen = models.ImageField(upload_to='images/', null=False)
>>>>>>> b1eb03d7aa2737231177b545073b6893f970fb3a

    def __str__(self):
        return self.nombre