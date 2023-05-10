from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import  ListCreateAPIView, DestroyAPIView
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Product
from .serializer import CategorySerializer, ProductSerializer

# class

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend)
    filterset_fields = ('category', 'title', 'descrition')

class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDestroyAPIView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer