from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryListAPIView, CategoryDestroyAPIView

router = DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('categories/', CategoryListAPIView.as_view())
    path('categories/<int:pk>/' CategoryListAPIView, )
]