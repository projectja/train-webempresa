from django.urls import path
from . import views 
from django.conf import settings

# esto se hacce para comprobar el modo DEBUG activo en el proyecto
# por que? porque para que las imagenes "MEDIA" funcionen en desarrollo necesitamos
# que el proyecto configurado en modo DEBUG
from django.conf import settings



urlpatterns = [
  # name='page' es el nombre del patrón, es el nombre que se indica en el url tag del template,
  # si cambio el nombre en el template url haciendo refrencia porj ejemplo a page.url, fallará porque
  # el nombre que se indica aquí es 'page', después views.page es el nombre de la vista
    path('<int:page_id>/<slug:page_slug>/',views.page,name='page')
     
        
]