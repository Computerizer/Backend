from dataclasses import field, fields
from rest_framework.serializers import ModelSerializer
from .models import Author, Post, Comment, LikeComment, LikePost

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class RecentPostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'  
        

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class LikePostSerializer(ModelSerializer):
    class Meta:
        model = LikePost
        fields = '__all__'

class LikeCommentSerializer(ModelSerializer):
    class Meta:
        model = LikeComment
        fields = '__all__'        