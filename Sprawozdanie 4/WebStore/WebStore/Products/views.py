from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

#Security
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    permission_classes = [IsAuthenticatedOrReadOnly]