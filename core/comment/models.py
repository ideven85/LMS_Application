from django.conf import settings
from django.db import models

from core.abstract.models import AbstractModel, AbstractManager
from core.post.models import Post
from core.user.models import User


class CommentManager(AbstractManager):
    pass

# Create your models here.
class Comment(AbstractModel):
    author = models.ForeignKey(to=User, on_delete=models.PROTECT)
    post = models.ForeignKey(to=Post, on_delete=models.PROTECT)
    body = models.TextField()
    edited=models.BooleanField(default=False)
    objects = CommentManager()
    def __str__(self):
        return self.author.name