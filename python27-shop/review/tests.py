from rest_frameworkt.serializers import ModelSerializer
from .models import Comment, Rating, Favorite

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        exclude = ("user",)

    def validate(self, attrs):
        super().validate(attrs)
        attrs["user"] = self.context["request"].user
        return attrs

class RatingSerializer(ModelSerializer):
    class Meta:
        model = Comment
        exclude = ("user",)
        
    def validate(self, attrs):
        super().validate(attrs)
        attrs["user"] = self.context["request"].user
        return attrs

class FavoritSerializer(ModelSerializer):
    class Meta:
        model = Comment
        exclude = ("user",)
        
    def validate(self, attrs):
        super().validate(attrs)
        attrs["user"] = self.context["request"].user
        return attrs