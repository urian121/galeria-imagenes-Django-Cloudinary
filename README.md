# Galería de Imágenes con Cloudinary

Aplicación web que permite subir y gestionar imágenes usando Django y Cloudinary para el almacenamiento.


## Configuración

1. Instalar dependencias:
```bash
pip install -r requirements.txt
```

2. Configurar variables de entorno (crear archivo `.env`):
```
CLOUDINARY_CLOUD_NAME=tu-nombre-de-cloud
CLOUDINARY_API_KEY=tu-api-key
CLOUDINARY_API_SECRET=tu-api-secret
```

3. Aplicar migraciones:
```bash
python manage.py migrate
```

4. Ejecutar el servidor:
```bash
python manage.py runserver
```

## Uso

1. Acceder a la aplicación en `http://localhost:8000`
2. Subir imágenes usando el formulario en el lado izquierdo
3. Ver las imágenes en el grid del lado derecho
4. Eliminar imágenes usando el botón de eliminar
