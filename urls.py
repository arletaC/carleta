# En el archivo urls.py del proyecto principal
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ventas/', include('ventas.urls')),  # Reemplaza 'tu_app' con el nombre de tu aplicación
]
