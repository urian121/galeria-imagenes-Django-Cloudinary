from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Imagen
import cloudinary.uploader

def subir_imagen(request):    
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        imagen = request.FILES.get('imagen')
        
        if titulo and imagen:
            try:
                cloudinary.uploader.upload(imagen)
                Imagen.objects.create(titulo=titulo, imagen=imagen)
                messages.success(request, 'Imagen subida exitosamente')
                return redirect('galeria')
            except Exception as e:
                messages.error(request, f'Error al subir la imagen: {str(e)}')
        else:
            messages.error(request, 'Debes proporcionar un título y una imagen')

    imagenes = Imagen.objects.all()
    return render(request, 'index.html', {
        'imagenes': imagenes
    })

def eliminar_imagen(request, imagen_id):
    imagen = get_object_or_404(Imagen, id=imagen_id)
    
    try:
        cloudinary.uploader.destroy(imagen.imagen.public_id)
        imagen.delete()
        messages.success(request, 'Imagen eliminada exitosamente')
    except Exception as e:
        messages.error(request, f'Error al eliminar la imagen: {str(e)}')
    
    return redirect('galeria')
