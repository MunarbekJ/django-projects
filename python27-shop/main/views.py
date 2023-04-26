# from django.shortcuts import render

# # Create your views here.


from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import  ListCreateAPIView, DestroyAPIView

from .models import Category, Product
from .serializer import CategorySerializer, ProductSerializer

# class

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryListAPIView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDestroyAPIView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer