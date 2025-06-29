from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Ruta inicial no lleva nada entre las comillas
    path('', include('home.urls')), # Manda a llamar al archivo urls de la app home
    path('api/v1/', include('ejemplo.urls')) # localhost/api/v1/recetas
]
