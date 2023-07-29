from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import action

from MainContent.abstractions.viewSets import AbstractViewSet 
from MainContent.Post.models.post import Post 
from MainContent.Post.serializers.postSerializer import PostSerializer



class PostViewSet(AbstractViewSet):

    http_method_names = ('post', 'get', 'put', 'delete')   
    permission_classes = (IsAuthenticated,)   
    serializer_class = PostSerializer
    parser_classes = (MultiPartParser, FormParser)
    
    def get_queryset(self):       
        return Post.objects.all()

    def get_object(self):       
        
        obj = Post.objects.get_object_by_public_id(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj
    
    def create(self, request, *args, **kwargs):       
        serializer = self.get_serializer(data = request.data)       
        serializer.is_valid(raise_exception=True)       
        self.perform_create(serializer)       
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(methods=['post'], detail=True)   
    def like(self, request, *args, **kwargs):       
        post = self.get_object()       
        user = self.request.user
        if user.has_disliked(post):
            user.remove_dislike(post)
        user.like(post)
        serializer = self.serializer_class(post, context= {'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=True)   
    def dislike(self, request, *args, **kwargs):       
        post = self.get_object()       
        user = self.request.user
        if user.has_liked(post):
            user.remove_like(post)
        user.dislike(post)
        serializer = self.serializer_class(post, context= {'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['delete'], detail=True) 
    def delete_like(self, request, *args, **kwargs):
        post = self.get_object()       
        user = self.request.user
        user.remove_like(post)
        serializer = self.serializer_class(post)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['delete'], detail=True) 
    def delete_dislike(self, request, *args, **kwargs):
        post = self.get_object()       
        user = self.request.user
        user.remove_dislike(post)
        serializer = self.serializer_class(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
