# Importaciones:
from django.urls import path
from ejemplo.views import Class_Ejemplo

urlpatterns = [
    path('ejemplo', Class_Ejemplo.as_view()) # as_view manda a llamar a todos los metodos de la clase
]