# Importaciones:
from django.db import models
from autoslug import AutoSlugField

# Clase donde se validaran los datos que se reciban
class Categoria(models.Model):

    # Campos de la base de datos:
    nombre = models.CharField(max_length = 100, null = False)
    # El slug sirve para tener URLs limpias y fáciles de leer, usando texto representativo del contenido.
    slug = AutoSlugField(populate_from = 'nombre')

    # LO SIGUIENTE SE AGREGA POR BUENAS PRACTICAS DE PROGRAMACION:

    # Campo que queremos siempre se muestre:
    def __str__(self):
        return self.nombre
    
    # Indica el nombre de la tabla con el que queramos que aparezca en el administrador de Django
    class Meta:
        # Nombre de la tabla:
        db_table = 'categorias'
        # Titulos de la tabla:
        verbose_name = 'Categoria'
        verbose_name = 'Categorias'




