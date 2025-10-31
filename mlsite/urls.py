from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(_request):
    # Página simple para comprobar que el backend responde
    return HttpResponse(
        "<h2>Servidor Django activo 🚀</h2><p>OK / Render</p>",
        content_type="text/html",
    )

def health(_request):
    return HttpResponse("OK", content_type="text/plain")

urlpatterns = [
    path("", home, name="home"),            # ✅ evita 500 en la raíz
    path("health/", health, name="health"), # para monitoreo si quieres
    path("admin/", admin.site.urls),
    path("api/", include("ml.urls")),       # ✅ monta las rutas del app ml bajo /api/
]