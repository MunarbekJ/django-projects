from rest_framework.serializers import ModelSerializer
from .models import Post
from review.serializers import CommentSerailizer


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance:Post):
        rep = super().to_representation(instance)
        #rep[;'likes]
        rep['likes'] = instance.likes.all().count()
        return rep
        comments = instance.comments.all() # все комменты данного поста 
        rep['comments'] = CommentSerailizer(comments, many=True).data
        return rep