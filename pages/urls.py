from django.urls import path
from . import views 
from django.conf import settings

# esto se hacce para comprobar el modo DEBUG activo en el proyecto
# por que? porque para que las imagenes "MEDIA" funcionen en desarrollo necesitamos
# que el proyecto configurado en modo DEBUG
from django.conf import settings



urlpatterns = [
  
    path('<int:page_id>/<slug:page_slug>/',views.page,name='page')
     
        
]