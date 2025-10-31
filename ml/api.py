from django.urls import path
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .services import predict_insurance, predict_diabetes


def _get_payload(request):
    """
    Acepta POST (JSON en request.data) y GET (query params).
    """
    if request.method == "POST":
        return request.data
    # GET → usar query params como dict simple
    return request.query_params


@api_view(["GET", "POST"])
def predict_insurance_api(request):
    try:
        payload = _get_payload(request)
        charges = predict_insurance(payload)  # tu función actual
        return Response({"charges": charges}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(
            {"error": f"predict_insurance failed: {e.__class__.__name__}: {e}"},
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(["GET", "POST"])
def predict_diabetes_api(request):
    try:
        payload = _get_payload(request)
        result = predict_diabetes(payload)  # tu función actual (debe devolver dict)
        # si tu función devuelve algo no-serializable, conviértelo aquí:
        return Response(result, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(
            {"error": f"predict_diabetes failed: {e.__class__.__name__}: {e}"},
            status=status.HTTP_400_BAD_REQUEST,
        )


urlpatterns = [
    path("predict/insurance", predict_insurance_api),
    path("predict/diabetes", predict_diabetes_api),
]