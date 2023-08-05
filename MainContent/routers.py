# Adding routers
#from rest_framework import routers
from rest_framework_nested import routers

from MainContent.User.viewsets import UserViewSet

from MainContent.Auth.viewsets.register import RegisterViewSet
from MainContent.Auth.viewsets.login import LoginViewSet
from MainContent.Auth.viewsets.refresh import RefreshViewSet

from MainContent.Post.viewSets import PostViewSet
from MainContent.Comment.viewset import CommentViewSet


router = routers.SimpleRouter()

router.register(r'user', UserViewSet, basename='user')

router.register(r'auth/register', RegisterViewSet, basename='auth-register')
router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')

router.register(r'post', PostViewSet, basename='post')
"""
Using   rest_framework_nested
GET    /api/post/post_pk/comment/ Lists all the comments of a post
GET    /api/post/post_pk/comment/ comment_pk/ Retrieves a specific comment 
POST   /api/post/post_pk/comment/ Creates a comment
PUT    /api/post/post_pk/comment/ comment_pk/ Modifies a comment
DELETE /api/post/post_pk/comment/ comment_pk/ Deletes a comment
"""
posts_router = routers.NestedSimpleRouter(router, r'post', lookup='post')
posts_router.register(r'comment', CommentViewSet, basename='post-comment') 

urls = router.urls + posts_router.urls