from django.urls import path
from . import api  # asumiendo que tus endpoints están en ml/api.py

app_name = "ml"

urlpatterns = [
    # Diabetes (clasificación)
    path("predict/diabetes", api.predict_diabetes, name="predict_diabetes"),
    # Costos de seguro (regresión)
    path("predict/insurance", api.predict_insurance, name="predict_insurance"),
]