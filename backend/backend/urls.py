from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Ruta inicial no lleva nada entre las comillas
    path('', include('home.urls')), # Manda a llamar al archivo urls de la app home
    path('api/v1/', include('ejemplo.urls')) # localhost/api/v1/recetas
]

# Url para configuracion de los archivos que se van a mostrar
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
