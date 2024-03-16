from django.conf import settings
from django.db import models
from django.utils import timezone

from core.abstract.models import AbstractManager, AbstractModel


# Create your models here.

class PostManager(AbstractManager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)

class Post(AbstractModel):
    class Status(models.TextChoices):
        PUBLISHED = 'PF', 'Published'
        DRAFT = 'DF', 'Draft'
    title = models.CharField(max_length=255, unique=True)
    author = models.ForeignKey(to="core_user.User", on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    edited =models.BooleanField(default=False)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    objects = PostManager()
    def __str__(self):
        return self.title + " by " + self.author.name

    class Meta:
        db_table="'core.post'"
        ordering = ["-publish"]
        indexes = [
            models.Index(fields=['-publish'])
        ]

