from django.urls import path
from .views import *

urlpatterns = [
    path('contacto', Clase_1.as_view()),
]