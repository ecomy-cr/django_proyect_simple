from django.contrib import admin
from django.urls import path

from app.views import inicio, exito


urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', inicio),
    path('exito/', exito)
]
