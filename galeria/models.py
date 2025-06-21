from django.db import models

class Imagen(models.Model):
    titulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='galeria/')

    def __str__(self):
        return self.titulo
