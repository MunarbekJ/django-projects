from rest_framework.serializers import ModelSerializer
from .models import Category, Product
class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        