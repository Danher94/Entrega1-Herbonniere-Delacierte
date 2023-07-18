from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Poema(models.Model):
    autor = models.CharField(max_length= 20)
    titulo = models.CharField(max_length= 20)
    contenido = RichTextField()
    fecha_publicacion = models.DateField(null=True)
    portada = models.ImageField(upload_to='portadas', null=True, blank=True)
    
    def __str__(self):
        return f'Titulo: {self.titulo} | Autor: {self.autor} '