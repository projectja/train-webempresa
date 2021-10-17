from django.db import models

# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length= 200, verbose_name="Tituloverbose")
    subtitle = models.CharField(max_length = 200, verbose_name="Subtituloverbose")
    content =  models.TextField(verbose_name="contenidoverbose")
    image = models.ImageField(verbose_name="imageverbose", upload_to='services',null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name = "fecha de creacion")
    updated_at = models.DateTimeField(auto_now=True, verbose_name = "fecha de edicion")

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "servicios"
        ordering = ['created']

    def __str__(self):
        return self.title
    