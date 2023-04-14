# from django.db import models
# from post.models import Post, User


# class Like(models.Model):
#     user = models.ForeignKey(User, related_name='like', on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, related_name='like', on_delete=models.CASCADE)

from django.db import models
from post.models import Post, User


class Like(models.Model):
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)