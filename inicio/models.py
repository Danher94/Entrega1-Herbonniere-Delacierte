from django.db import models

# Create your models here.

class Poema(models.Model):
    autor = models.CharField(max_length= 20)
    titulo = models.CharField(max_length= 20)
    fecha_publicacion = models.DateField(null=True)
    portada = models.ImageField(upload_to='portadas', null=True, blank=True)
    
    def __str__(self):
        return f'Autor: {self.autor}  |  Titulo: {self.titulo}'