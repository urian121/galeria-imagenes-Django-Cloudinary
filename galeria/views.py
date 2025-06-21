from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import ImagenForm
from .models import Imagen

def subir_imagen(request):
    if request.method == 'POST':
        form = ImagenForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('galeria')
    else:
        form = ImagenForm()

    imagenes = Imagen.objects.all()
    return render(request, 'galeria/index.html', {'form': form, 'imagenes': imagenes})
