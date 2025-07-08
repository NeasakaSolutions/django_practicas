# Importaciones
from rest_framework.views import APIView
from django.http.response import JsonResponse
from categorias.models import Categoria
from rest_framework.response import Response
from categorias.serializers import CategoriaSerializer
from http import HTTPStatus
from django.http import Http404

# Clase sin argumentos
class Clase1(APIView):
    
    def get(self, request):
        # select * from categorias order by id desc;
        data = Categoria.objects.order_by('-id').all()
        # Mandamos a llamar al serializer
        datos_json = CategoriaSerializer(data, many = True)
        return JsonResponse({"data": datos_json.data}, status = HTTPStatus.OK)
    
    def post(self, request):
        pass
    

# Clase con argumentos, para busquedas por medio de id
class Clase2(APIView):

    def get(self, request, id):
        try:
            # select * from categorias where id = 4;
            data = Categoria.objects.filter(pk = id).get() # pk (primary key)
            return JsonResponse({"data": {"id": data.id, "nombre": data.nombre, "slug": data.slug}}, status = HTTPStatus.OK)
        except Categoria.DoesNotExist:
            raise Http404
