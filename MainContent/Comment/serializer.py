
from rest_framework import serializers 
from rest_framework.exceptions import ValidationError

from MainContent.abstractions.serializers import AbstractSerializer 
from MainContent.User.serializers import UserSerializer 

from MainContent.Post.models.post import Post
from MainContent.User.models import User
from MainContent.Comment.models import Comment


class CommentSerializer(AbstractSerializer):   
    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='public_id')   
    post = serializers.SlugRelatedField(queryset=Post.objects.all(), slug_field='public_id')
    
    def to_representation(self, instance):       
        rep = super().to_representation(instance)       
        author = User.objects.get_object_by_public_id(rep["author"])       
        rep["author"] = UserSerializer(author).data
        return rep

    def update(self, instance, validated_data):       
        if not instance.edited:           
            validated_data['edited'] = True       
        instance = super().update(instance, validated_data)       
        return instance 
    
    
    def validate_post(self, value):   
        if self.instance:
            #if already instance exists return that instance and not the value, else return the value       
            return self.instance.post   
        return value 
    
    class Meta:       
        model = Comment       
        # List of all the fields that can be included in a       
        # request or a response       
        fields = ['id', 'post', 'author', 'body', 'edited', 'created', 'updated']       
        read_only_fields = ["edited"]
