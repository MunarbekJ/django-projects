from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from .models import Comment, Rating, Favorite
from .serializers import CommentSErializer, RatingSerializer, FavoriteSerializer

class CommentViewSet(mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSErializer
    permission_classes = [IsAuthenticated]


class CommentViewSet(mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSErializer
    permission_classes = [IsAuthenticated]

class AddRatingAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=RatingSerializer())

    def post(self, request):
        ser = RatingSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data, status=201)

