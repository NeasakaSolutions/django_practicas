# Importaciones:
from django.urls import path
from home.views import home_inicio

urlpatterns = [
    # Ruta inicial no lleva nada entre las comillas
    path('', home_inicio) # Manda a llamar a la funcion home_inicio
]