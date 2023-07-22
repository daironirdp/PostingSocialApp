from django.contrib import admin

# Register your models here.
from django.contrib import admin
from MainContent.Post.models.post import Post
from MainContent.Post.models.image import Image_Post
from MainContent.Post.models.video import Video_Post

#Creating the admin inline clases for Image and Video
class Inline_Image(admin.TabularInline):
    model = Image_Post
    extra = 1

class Inline_Video(admin.TabularInline):
    model = Video_Post
    extra = 1

# Register your models here.
class ManagerAdminPost(admin.ModelAdmin):
    inlines = (Inline_Image, Inline_Video)

#Registering the Post model with the post manager in the django admin panel 
admin.site.register(Post, ManagerAdminPost)

admin.site.register(Image_Post)
admin.site.register(Video_Post)