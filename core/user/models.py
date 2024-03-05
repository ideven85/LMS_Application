from django.db import models

# Create your models here.
import uuid

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.http import Http404

from hashlib import pbkdf2_hmac

from core.abstract.models import AbstractManager, AbstractModel


# Create your models here.

class UserManager(BaseUserManager,AbstractManager):
    # key = pbkdf2_hmac(
    #     hash_name='sha1',
    #     password=b"somekeyvalue",
    #     salt=b"somekeyvalue",
    #     iterations=12345,
    #     dklen=32
    # )

    def create_user(self,username,email,password=None,**extra_fields):
        if not username:
            raise TypeError('Users must have an username')
        if not email:
            raise TypeError('Users must have an email')
        if not password:
            raise TypeError('Users must have a password')
        user = self.model(username=username,email=self.normalize_email(email),**extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username,email,password,**extra_fields):
        if not username:
            raise TypeError('Users must have an username')
        if not email:
            raise TypeError('Users must have an email')
        if not password:
            raise TypeError('Users must have a password')
        user = self.create_user(username,email,password,**extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser, PermissionsMixin,AbstractModel):
    username = models.CharField(db_index=True,max_length=255,unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(db_index=True,unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    posts_liked = models.ManyToManyField(to="core_post.Post", related_name="liked_by",null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = UserManager()

    # I think I should read properly documentation..
    # Why are we putting logic in domain layer?
    def like_post(self,post):
        return self.posts_liked.add(post)

    def remove_liked_post(self,post):
        return self.posts_liked.remove(post)

    def has_liked_post(self,post):
        return self.posts_liked.filter(pk=post.pk).exists()
    def __str__(self):
        return self.first_name + ' ' + self.last_name

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'

