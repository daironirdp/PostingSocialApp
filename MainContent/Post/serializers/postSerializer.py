from rest_framework import serializers 
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CurrentUserDefault

from django.core.validators import FileExtensionValidator, MaxValueValidator

from MainContent.Post.models.post import Post 
from MainContent.User.models import User
from MainContent.Post.models.image import Image_Post
from MainContent.Post.models.video import Video_Post

from MainContent.abstractions.serializers import AbstractSerializer 
from MainContent.Post.serializers.attachmentSerializer import ImageSerializer
from MainContent.Post.serializers.attachmentSerializer import VideoSerializer
from MainContent.Post.serializers.validators import SizeValidator
from MainContent.User.serializers import UserSerializer



class PostSerializer(AbstractSerializer):

    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='public_id')
    
    images = ImageSerializer(many=True, read_only=True, required=False)
    videos = VideoSerializer(many=True, read_only=True, required=False)
    
    uploaded_images = serializers.ListField(child = serializers.ImageField( max_length = 100000, required=False, 
                        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png','jfif']), SizeValidator(300000)]), 
                        write_only=True, required=False) 
    
    uploaded_videos = serializers.ListField(child = serializers.FileField( max_length = 1000000, 
                        validators=[FileExtensionValidator(allowed_extensions=['mp4', 'mkv', 'mpg','avi']), SizeValidator(50000000)]), 
                        write_only=True, required=False)

    liked = serializers.SerializerMethodField()   
    likes_count = serializers.SerializerMethodField()

    disliked = serializers.SerializerMethodField()
    dislikes_count = serializers.SerializerMethodField()
            
    def validate_author(self, value):               
        # value has the value of the post you want to create
        # self.context['request'].user contains the value of the authenticated user  
        if self.context["request"].user != value:           
            raise ValidationError("You can't create a post for another user.")    
        return value
    

    def videoImageCreate(self, post, attachments, database):
        
        for attachment in attachments:
            #create the attachment objects in the database
            database.objects.create(post=post, attachment= attachment)



    def to_representation(self, instance):       
        rep = super().to_representation(instance)
        author = User.objects.get_object_by_public_id(rep["author"])       
        rep["author"] = UserSerializer(author).data
        return rep 
    
    
    def create(self, validated_data):
        #retrive the validated attachment data from the body of the request
        images_data = False
        videos_data = False
        
        if "uploaded_images" in validated_data:
            images_data = validated_data.pop('uploaded_images')

        
        if "uploaded_videos" in validated_data:
            videos_data = validated_data.pop('uploaded_videos')
        
        #Create the post in the database
        post = Post.objects.create(**validated_data)
        
        if images_data:
            #create the attachment video objects in the database
            self.videoImageCreate(post, images_data, Image_Post)

        if videos_data:
            #create the attachment video objects in the database
            self.videoImageCreate(post, videos_data, Video_Post)

        return post

    def update(self, instance, validated_data):
        """Rewritting the update functionality to allow us to change the edited value """    
    
        if not instance.edited:           
            validated_data['edited'] = True
        instance = super().update(instance, validated_data)
        return instance 


    def get_liked(self, instance):
        
        request = self.context.get('request', None)
    
        if request is None or request.user.is_anonymous:           
            return False
        return request.user.has_liked(instance)

    def get_disliked(self, instance):
        
        request = self.context.get('request', None)
    
        if request is None or request.user.is_anonymous:           
            return False
        return request.user.has_disliked(instance)
    
    
    def get_likes_count(self, instance):       
        return instance.liked_by.count()

    def get_dislikes_count(self, instance):       
        return instance.disliked_by.count()

    
        
    class Meta:       
        model = Post       
        # List of all the fields that can be included in a       
        # request or a response       
        fields = ['id', 'title','author', 'body', 'images','videos',
        'edited', 'created', 'updated', 'uploaded_videos', 'uploaded_images', 'liked', 'likes_count','disliked', 'dislikes_count',]       
        read_only_fields = ["edited"]
