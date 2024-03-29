from distutils.command.upload import upload
from typing import Iterable, Optional
from django.db import models
from Oauth.models import CustomUser
from tinymce.models import HTMLField


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=64)
    date_of_birth = models.DateField()
    description = models.TextField()
    profile_picture = models.ImageField(upload_to = r'Blog/profile_picture')
    instagram = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    linkedIn = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    youtube = models.URLField(null=True, blank=True)
    gitHub = models.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Post(models.Model):
    status_choices = [
        ('Archived', 'archived'),
        ('Published', 'published'),
        ('Unpublished', 'unpublished')
    ]

    title = models.CharField(max_length=150)
    slug = models.CharField(max_length=25, help_text='A dash should be put after each word')
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    body = HTMLField()
    description = models.TextField(default=None)
    image = models.ImageField(upload_to = r'Blog/thumbnails')
    status = models.CharField(choices = status_choices, max_length=15)
    add_date  = models.DateTimeField(auto_now_add=True)
    publish_date  = models.DateTimeField(null=True, blank=True)
    #likes = models.ManyToManyField(CustomUser, related_name='post_likes', blank=True)
    #dislikes = models.ManyToManyField(CustomUser, related_name='post_dislikes', blank=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.title}'
    
    def get_likes_num(self):
        return self.likes.count()
    
    def get_dislikes_num(self):
        return self.dislikes.count()

    def get_absolute_url(self):
        return f'post/{self.slug}'


class Post_Image(models.Model):
    title= models.CharField(max_length= 60)
    image = models.ImageField(upload_to = r'Blog/media')
    post = models.ForeignKey(Post, on_delete= models.CASCADE)

    def __str__(self):
        return f'{self.post.title}: {self.title}'
    

class Category(models.Model):
    image = models.ImageField(upload_to = r'Blog/media')
    title = models.CharField(max_length = 120)
    posts = models.ManyToManyField(Post, blank=True)

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None)    
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(CustomUser, related_name='comment_likes', blank= True)



    def __str__(self):
        return f'{self.user}({self.post.title}): {self.body}'
    
    def get_likes_num(self):
        return self.likes.count()


# class LikePost(models.Model):
#     like_choices = [
#         ('Liked', 'liked'),
#         ('Disliked', 'disliked'),
#         ('', '')
#     ]

#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     like_state = models.CharField(choices=like_choices, max_length=15)
#     user = models.ForeignKey(CustomUser, on_delete= models.CASCADE)

#     def __str__(self):
#         return f'{self.post.title}: {self.user}'


class LikeComment(models.Model):

    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)  
    user = models.ForeignKey(CustomUser, on_delete= models.CASCADE)

#     def __str__(self):
#         return f'{self.user}: {self.comment.body}'    