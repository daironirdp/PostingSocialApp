from django.db import models

# Create your models here.
from MainContent.Post.models.post import Post
from MainContent.Post.models.attachment import Attachment

class Image_Post(Attachment):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='images')
    attachment = models.ImageField(upload_to="Post/attachments/images/")

    def __str__(self):
        return f'{self.attachment.name}'

    class Meta:       
        db_table = "'MainContent.Post.Attachment.Image'"