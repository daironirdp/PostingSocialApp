from rest_framework import serializers

from MainContent.Post.models.image import Image_Post
from MainContent.Post.models.video import Video_Post

from MainContent.Post.models.post import Post

class VideoSerializer(serializers.ModelSerializer):   
    
    def validate_attachment(self,value):
        return value


    class Meta:       
        model = Video_Post
        fields = ['post', 'attachment', 'id']
        read_only_fields = ['post', 'id']         


class ImageSerializer(serializers.ModelSerializer):   
    
    def validate_attachment(self,value):
        return value


    class Meta:       
        model = Image_Post
        fields = ['post', 'attachment', 'id']
        read_only_fields = ['post', 'id']         