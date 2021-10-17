from django.apps import AppConfig


class ServicesConfig(AppConfig):
    name = 'services'
    # para traducir el nombre de la aplicación a español usamos lo que viedne a continuación 
    # lo definimos aqui el verbose name y nos vamos a installed_app del setting y 
    # hacemos referencia a services.apps (el apps viene de este fichero appy.py)
    # e indicamos la clase ServicesConfig
    verbose_name = 'Gestor de servicios'


