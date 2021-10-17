
from django.db import models
from django.db.models.fields.related import create_many_to_many_intermediary_model

# Create your models here.

class Link(models.Model):
    key=models.SlugField(verbose_name="Nombre clave",max_length=100,unique=True)
    name=models.CharField(verbose_name="Red social", max_length=200)
    url=models.URLField(verbose_name="Enlace",max_length=200, null=True, blank=True)
    created=models.DateTimeField(verbose_name="Fecha de creación",auto_now_add=True)
    updated=models.DateTimeField(verbose_name="Fecha de edición",auto_now=True)

    class Meta:
        verbose_name="enlace"
        verbose_name_plural = "enlaces"
        ordering = ['name']

    def __str__(self):
        return self.name

