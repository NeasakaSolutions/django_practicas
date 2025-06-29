# Importaciones:
from django.urls import path
from ejemplo.views import Class_Ejemplo
from ejemplo.views import Class_Ejemplo_Parametros

urlpatterns = [
    path('ejemplo', Class_Ejemplo.as_view()), # as_view manda a llamar a todos los metodos de la clase
    # Se le pueden pasar argumentos con la identacion "diamante" <>, para pasar mas de uno se puede hacer asi:
    # <int:id>/<string:slug>   Se pueden usar otros tipos de datos
    # IMPORTANTE: NO DEJAR ESPACIOS EN LOS DIAMANTES
    path('ejemplo/<int:id>', Class_Ejemplo_Parametros.as_view())
]