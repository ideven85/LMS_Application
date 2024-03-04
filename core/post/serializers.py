from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from core.abstract.serializers import AbstractSerializer
from core.post.models import Post
from core.user.models import User
from core.user.serializers import UserSerializer


class PostSerializer(AbstractSerializer):
    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='public_id')
    liked = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    def get_liked(self,instance):
        request = self.context.get('request',None)
        if not request or request.user.is_anonymous:
            return False
        return request.user.has_liked_post(instance)

    def get_likes_count(self,instance):
        return instance.liked_by.count()


    def validate_author(self, value):
        if self.context['request'].user != value:
            raise ValidationError('You do not have permission to create this post for another user')
        return value
    class Meta:
        model = Post
        fields = ['id','author','title','body','liked','likes_count','created','updated','edited']
        read_only_fields = ['edited']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # for key, value in representation.items():
        #     print(key,value)
        author = User.objects.get_object_by_public_id(representation['author'])
        representation['author'] = UserSerializer(author).data
        n = representation['author']
        # for key, value in n.items():
        #     print(key,value)
        #representation['author'] = n['first_name'] + ' ' + n['last_name'] # Modified Representation of author to just Name
        #representation['author'] = representation['author']['first_name'] + ' ' + representation['author']['last_name']
        return representation
    def update(self, instance, validated_data):
        if not instance.edited:
            validated_data['edited'] =True
        instance=super().update(instance,validated_data)
        return instance


