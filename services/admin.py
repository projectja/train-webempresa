from django.contrib import admin
# para que sea accesible desde panel de control: 1.- importo el modelo
from .models import Service

# Register your models here.
# 2.- crear  una configuracion basica para el administrador, en este caso es para campos solo lectura
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated_at')

admin.site.register(Service, ServiceAdmin)
