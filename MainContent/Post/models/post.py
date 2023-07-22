from django.db import models

# Create your models here.
from MainContent.abstractions.models import AbstractModel, AbstractManager
from MainContent.User.models import User

class PostManager(AbstractManager):   
    pass

class Post(AbstractModel):   

    author = models.ForeignKey(to=User, on_delete=models.CASCADE)   
    title = models.CharField(max_length=250, null=False, default="This is the title")
    body = models.TextField(null=False, max_length=500)   
    edited = models.BooleanField(default=False)
    
    objects = PostManager()   
    
    def __str__(self):       
        return f"{self.author.name}"

    class Meta:       
        db_table = "'MainContent.Post'" 
