from django.db import models

# Create your models here.
from MainContent.abstractions.models import AbstractModel, AbstractManager
from MainContent.Post.models.post import Post

class AttachmentManager(AbstractManager):   
    pass

class Attachment(models.Model):   
    
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='videos')
    attachment = models.FileField(upload_to="Post/attachments/videos/")
    
    objects = AttachmentManager()   
    

    class Meta:       
        db_table = "'MainContent.Post.Attachment'"
        abstract = True
