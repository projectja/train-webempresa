
from django.db import models
from django.db.models.fields.related import create_many_to_many_intermediary_model

# Create your models here.

class Page(models.Model):   
    title=models.CharField(verbose_name="Titulo", max_length=200)
    content=models.URLField(verbose_name="Contenido" ,max_length=200, null=True, blank=True)
    created=models.DateTimeField(verbose_name="Fecha de creación",auto_now_add=True)
    updated=models.DateTimeField(verbose_name="Fecha de edición",auto_now=True)

    class Meta:
        verbose_name="pagina"
        verbose_name_plural = "paginas"
        ordering = ['title']

    def __str__(self):
        return self.title

