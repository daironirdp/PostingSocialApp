from django.db import models

# Create your models here.

import uuid

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

from MainContent.abstractions.models import AbstractManager, AbstractModel

class UserManager(BaseUserManager, AbstractManager):


    def create_user(self, username, email, password=None, **kwargs):
        """Create and return a `User` with an email, phone number, username and password."""

        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email.')

        if password is None:
            raise TypeError('User must have a password.')

        user = self.model(username=username,
                          email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, email="example@gmail.com", **kwargs):
        """Create and return a `User` with superuser (admin) permissions."""
        if password is None:
            raise TypeError('Superusers must have a password.')

        if email is None:
            raise TypeError('Superusers must have an email.')

        if username is None:
            raise TypeError('Superusers must have an username.')

        user = self.create_user(username, email, password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractModel, AbstractBaseUser, PermissionsMixin):

    username = models.CharField(db_index=True, max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    #bio = models.CharField(max_length=255)
    # avatar = models.CharField(max_length=255)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    posts_liked = models.ManyToManyField('mainContent_post.Post', related_name="liked_by")
    posts_disliked = models.ManyToManyField('mainContent_post.Post', related_name="disliked_by") 

    USERNAME_FIELD = 'email'

    USERNAME_FIELD = 'email'   
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    def like(self, post):       
        """Like `post` if it hasn't been done yet"""       
        return self.posts_liked.add(post)

    def dislike(self, post):       
        """Dislike `post` if it hasn't been done yet"""       
        return self.posts_disliked.add(post)
    
    def remove_like(self, post):           
        """Remove a like from a `post`"""       
        return self.posts_liked.remove(post)
    
    def remove_dislike(self, post):
        """ Remove a dislike from a 'post' """
        return self.posts_disliked.remove(post)
    
    def has_liked(self, post):       
        """Return True if the user has liked a `post`; else False"""       
        return self.posts_liked.filter(pk=post.pk).exists()

    def has_disliked(self, post):
        """Return True if the user has disliked a 'post' """
        return self.posts_disliked.filter(pk=post.pk).exists()
