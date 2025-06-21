from django.urls import path
from galeria.views import subir_imagen, eliminar_imagen

urlpatterns = [
    path('', subir_imagen, name='galeria'),
    path('eliminar/<int:imagen_id>/', eliminar_imagen, name='eliminar_imagen'),
]