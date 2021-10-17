"""webempresa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http.request import MediaType
from django.urls import path
from core import views 
from django.conf import settings

# esto se hacce para comprobar el modo DEBUG activo en el proyecto
# por que? porque para que las imagenes "MEDIA" funcionen en desarrollo necesitamos
# que el proyecto configurado en modo DEBUG
from django.conf import settings

import core

urlpatterns = [
    #path('admin/', admin.site.urls),
    # Path del core
    path('',views.home, name="home"),
    path('historia/',views.about, name="about"),
    path('servicios/',views.services, name="services"),
    path('visitanos/',views.store, name="store"),
    path('contacto/',views.contact, name="contact"),    
        
    
        
]

# nos imoprtamos los staticos para poder servirlos cuando haya peticioens
# es un modo complejo en modo DEBUJ pero a dia de hoy no hay otra manera de hacerlo
if settings.DEBUG:
    from django.conf.urls.static import static
    # lo siguiente es para indicar donde quermoos que ser vicrva los ficheros MediaTyp
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


''' Inicio home/
Historia about/
Servicios services/
Visítanos store/
Contacto contact/
Blog blog/
Sample sample/ (esta es para páginas de prueba) '''



