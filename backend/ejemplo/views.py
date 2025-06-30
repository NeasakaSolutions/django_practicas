# Importaciones necesarias
# APIView es una clase base proporcionada por Django REST Framework (DRF)
# que permite crear endpoints RESTful con métodos HTTP como GET, POST, PUT y DELETE
from rest_framework.views import APIView
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import Http404
from django.core.files.storage import FileSystemStorage
from datetime import datetime
import os

# Creacion de clases:
class Class_Ejemplo(APIView):
    '''Clase que muestra la utilizacion de los distintos metodos que nos ofrece python'''

    # Método GET: se utiliza para obtener o listar registros
    def get(self, request):
        # Se obtiene los parametros del metodo request y se accede solo con los metodos GET y get
        # Por buenas practicas se pone el segundo parametro None
        '''
        return HttpResponse(f"Metodo GET | " 
                            f"id = {request.GET.get('id', None)} | "
                            f"slug = {request.GET.get('slug', None)}")
        '''

        # Forma mas segura para evitar dar informacion a los hackers
        return JsonResponse({"estado": "ok", "mensaje" : f"Metodo GET | " 
                                f"id = {request.GET.get('id', None)} | "
                                f"slug = {request.GET.get('slug', None)}"}, 
                                status = 200)

    # Método POST: se utiliza para crear nuevos registros en el servidor
    def post(self, request):
        if request.data.get("correo") == None or request.data.get("password") == None:
            raise Http404
        else:
            return JsonResponse({"estado":"ok", "mensaje": 
                                f"Metodo POST | correo = {request.data.get("correo")} |" 
                                f"password = {request.data.get("password")}"}, 
                                status = 201)

    
class Class_Ejemplo_Parametros(APIView):

    def get(self, request, id): # id es el parametro de la url
        return HttpResponse(f"Metodo GET | parametro = {id}")

    # Método PUT: se utiliza para editar o actualizar registros existentes
    def put(self, request, id): # id es el parametro de la url
        return HttpResponse(f"Metodo PUT | parametro = {id}")

    # Método DELETE: se utiliza para eliminar registros existentes  
    def delete(self, request, id): # id es el parametro de la url
        return HttpResponse(f"Metodo DELETE | parametro = {id}")

# Clase para subir archivos al servidor:
class Class_EjemploUpload(APIView):

    def post(self, request):

        # Variables:
        fs = FileSystemStorage()
        # Asigna un nombre unico al archivo
        fecha = datetime.now()
        foto = f"{datetime.timestamp(fecha)}{os.path.splitext(str(request.FILES['file']))[1]}"

        # Guardar archivo
        # El primer argumento es para ubicar la carpeta donde se guardara el archivo y como se llamara el archivo
        fs.save(f"ejemplo/{foto}", request.FILES['file'])
        # Guardar
        fs.url(request.FILES['file'])

        return JsonResponse({"estado":"ok", "mensaje":"Se subio el archivo"})