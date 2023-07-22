from django.db import models

# Create your models here.
from MainContent.Post.models.attachment import Attachment

class Video_Post(Attachment):
    attachment = models.ImageField(upload_to="Post/attachments/images/")

    def __str__(self):
        return f'{self.attachment.name}'

    class Meta:       
        db_table = "'MainContent.Post.Attachment.Video'"