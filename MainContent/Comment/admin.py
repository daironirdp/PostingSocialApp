from django.contrib import admin
from MainContent.Comment.models import Comment

# Register your models here.

class ManagerAdminComment(admin.ModelAdmin):
    pass

#Registering the Comment model with the Comment manager in the django admin panel 
admin.site.register(Comment, ManagerAdminComment)