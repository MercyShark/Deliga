from rest_framework import serializers
from .models import Post
from drf_extra_fields.fields import Base64ImageField

class CreatePostSerializer(serializers.ModelSerializer):
    image = Base64ImageField()
    class Meta:
        model = Post
        fields = ('image','caption','latitude','longitude',)

    def create(self,validated_data):
        user = self.context.get('user')
        validated_data['user'] = user
        instance = Post.objects.create(**validated_data)
        return instance
        
class ShowPostSerializer(serializers.ModelSerializer):  
    image = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = "__all__"

    def get_image(self,post):
        return f'http://127.0.0.1:8000/{post.image}'

    