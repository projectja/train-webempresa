from django.contrib import admin
from django.http.request import MediaType
from django.urls import path
from django.conf import settings
from . import views

# esto se hacce para comprobar el modo DEBUG activo en el proyecto
# por que? porque para que las imagenes "MEDIA" funcionen en desarrollo necesitamos
# que el proyecto configurado en modo DEBUG
from django.conf import settings

import core

urlpatterns = [
    #path('admin/', admin.site.urls),
    # Path del core
    path('',views.blog, name="blog"),
  
    
        
]