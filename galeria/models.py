from django.db import models
from cloudinary.models import CloudinaryField

class Imagen(models.Model):
    titulo = models.CharField(max_length=100)
    imagen = CloudinaryField('imagen')

    def __str__(self):
        return self.titulo