from django.db import models

# Create your models here.
from MainContent.abstractions.models import AbstractModel, AbstractManager
from MainContent.User.models import User
from MainContent.Post.models.post import Post

class CommentManager(AbstractManager):   
    pass

class Comment(AbstractModel):   

    author = models.ForeignKey(to=User, on_delete=models.PROTECT) 
    post = models.ForeignKey(to=Post, on_delete=models.PROTECT)
    comment = models.TextField(null=False, max_length=500)   
    edited = models.BooleanField(default=False)
    
    objects = CommentManager()   
    
    def __str__(self):       
        return f"{self.author.name}"

    class Meta:       
        db_table = "'MainContent.Comment'" 
