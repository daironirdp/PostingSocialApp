# Adding routers
from rest_framework import routers

from MainContent.User.viewsets import UserViewSet

from MainContent.Auth.viewsets.register import RegisterViewSet
from MainContent.Auth.viewsets.login import LoginViewSet
from MainContent.Auth.viewsets.refresh import RefreshViewSet

from MainContent.Post.viewSets import PostViewSet


router = routers.SimpleRouter()

router.register(r'user', UserViewSet, basename='user')

router.register(r'auth/register', RegisterViewSet, basename='auth-register')
router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')

router.register(r'post', PostViewSet, basename='post')

urls = router.urls
