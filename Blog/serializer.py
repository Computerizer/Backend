from rest_framework.serializers import ModelSerializer

from .models import Author, Post, Post_Image, Comment, Category



class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class RecentPostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'description', 'image', 'status', 'publish_date', 'likes', 'dislikes', 'views']

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class ImagePostSerializer(ModelSerializer):
    class Meta:
        model = Post_Image
        fields = '__all__'
        

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

# class LikePostSerializer(ModelSerializer):
#     class Meta:
#         model = LikePost
#         fields = '__all__'

# class LikeCommentSerializer(ModelSerializer):
#     class Meta:
#         model = LikeComment
#         fields = '__all__'        