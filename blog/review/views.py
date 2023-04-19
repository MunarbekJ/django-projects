from rest_framework.decorators import api_view
from rest_framework.response import Response
# from rest_framework.
from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from .models import Like, Comment
from post.models import Post, User
from .serializers import CommentSerailizer

@api_view(['POST'])
def toggle_like(request, id):
    user = request.user
    if not user.is_authenticated:
        return Response(status=401)
    user_id = request.data.get('user')
    if not user_id: # user_id = None
        return Response({"user":["this field is required"]}, status=400)
    user = get_object_or_404(User, id=user_id)
    post = get_object_or_404(Post, id=id)
    if Like.objects.filter(user=user, post=post).exists():
        # если лайк есть, то удаляем его
        Like.objects.filter(user=user, post=post).delete()
    else:
        # если нет, создаем
        Like.objects.create(user=user, post=post)
    return Response('like')

class CreateCommentAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerailizer

class UpdateCommentAPIView(UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerailizer

class DeleteCommentAPIView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerailizer
    # permission_classes = [IsAuthenti]