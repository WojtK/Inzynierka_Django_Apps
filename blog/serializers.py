from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Post , Comment
from taggit.managers import TaggableManager


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'author', 'publish', 'status']


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'post', 'created', 'active']


class LoginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'post', 'created', 'active']