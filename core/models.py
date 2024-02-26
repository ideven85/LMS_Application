import uuid

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.http import Http404


# Create your models here.

class UserManager(BaseUserManager):
    def get_object_by_public_id(self, public_id):
        try:
            instance = self.get(public_id=public_id)
            return instance
        except (ObjectDoesNotExist,ValueError,TypeError):
            return Http404
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



class User(AbstractBaseUser, PermissionsMixin):
    public_id = models.UUIDField(db_index=True,unique=True, default=uuid.uuid4,editable=False)
    username = models.CharField(db_index=True,max_length=255,unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(db_index=True,unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

