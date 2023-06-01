from django.forms.models import model_to_dict

from products.models import Product
from products.serializers import ProductSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(["GET"])
def api_home(request, *args, **kwargs):
    
    instance = Product.objects.all().order_by("?").first()
    data = {}

    if instance:
        data = ProductSerializer(instance).data

    return Response(data, status=status.HTTP_200_OK)

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    else:
        return Response(serializer.errors )