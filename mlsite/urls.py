from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(_request):
    return HttpResponse("<h2>Servidor Django activo 🚀</h2><p>OK / Render</p>")

urlpatterns = [
    path("", home, name="home"),       # evita 500/404 en la raíz
    path("admin/", admin.site.urls),
    path("api/", include("ml.api")),   # monta los endpoints del archivo api.py
]