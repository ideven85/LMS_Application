from rest_framework import serializers

from core.abstract.serializers import AbstractSerializer
from core.user.models import User


class UserSerializer(AbstractSerializer):


    class Meta:
        model = User
        fields = ['id','username','email','first_name','last_name','password','created','updated','is_active']
        read_only_field = ['is_active']
