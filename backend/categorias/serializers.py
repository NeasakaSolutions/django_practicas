from rest_framework import serializers
from categorias.models import Categoria

class CategoriaSerializer(serializers.ModelSerializer):
     class Meta:
          # Categoria a la que se va a conectar
          model = Categoria
          # Campos que quieres que retornen
          fields = ("id", "nombre", "slug")
          # fields = '__all__' # Es lo mismo que lo de arriba
          # fields = ('__all__') # Es lo mismo que lo de arriba
