from django.conf import settings
from django.db import models

from core.abstract.models import AbstractManager, AbstractModel


# Create your models here.

class PostManager(AbstractManager):
    pass

class Post(AbstractModel):
    title = models.CharField(max_length=255, unique=True)
    author = models.ForeignKey(to="core_user.User", on_delete=models.CASCADE)
    body = models.TextField()
    edited =models.BooleanField(default=False)
    objects = PostManager()
    def __str__(self):
        return self.title + " by " + self.author.first_name

    class Meta:
        db_table="'core.post'"

