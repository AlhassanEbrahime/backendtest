from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Product
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import ProductSerializer
# Create your views here.

@api_view()
def product_list(request):
    return Response("Products")

@api_view()
def product_detail(request,id):
        product = get_object_or_404(Product,pk= id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)