from django.shortcuts import render, HttpResponse

# Create your views here.

''' Inicio home/
Historia about/
Servicios services/
Visítanos store/
Contacto contact/
Blog blog/
Sample sample/ (esta es para páginas de prueba) '''

def home(request):    
    return render(request,"core/home.html")

def about(request):
    return render(request,"core/about.html")

def services(request):
     return render(request,"core/services.html")

def store(request):
    return render(request,"core/store.html")

def contact(request):
     return render(request,"core/contact.html")

