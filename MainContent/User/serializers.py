from MainContent.abstractions.serializers import AbstractSerializer
from MainContent.User.models import User


class UserSerializer(AbstractSerializer):
    #This is a serializer to show and modify user data 
    
    class Meta:       
        model = User       
        fields = ['id', 'username', 'first_name', 
            'last_name', 'email', 'is_active', 'created', 'updated']
        read_only_field = ['is_active']
