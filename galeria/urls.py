from django.contrib import admin
from django.urls import path
from galeria.views import subir_imagen

urlpatterns = [
    path('', subir_imagen, name='galeria'),
]