from distutils.command.upload import upload
from django.db import models
from Oauth.models import CustomUser
# Create your models here.
class Author(models.Model):
    id = models.TextField(primary_key=True)
    name = models.CharField(max_length=64)
    date_of_birth = models.DateField()
    description = models.TextField()
    profile_picture = models.ImageField(upload_to = r'Computerizer/static/Blog/profile_picture')
    instagram = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    linkedIn = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    youtube = models.URLField(null=True, blank=True)
    gitHub = models.URLField(null=True, blank=True)



class Post(models.Model):
    status_choices = [
        ('Archived', 'archived'),
        ('Published', 'published'),
        ('Unpublished', 'unpublished')
    ]

    title = models.CharField(max_length=258)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    body = models.FilePathField(path=r'Blog\blogs')
    description = models.TextField(default=None)
    image = models.ImageField(upload_to = r'Computerizer/static/Blog/media')
    status = models.CharField(choices = status_choices, max_length=15)
    add_date  = models.DateTimeField(auto_now_add=True)
    publish_date  = models.DateTimeField(null=True, blank=True)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.title}'


class Category(models.Model):
    image = models.ImageField(upload_to = r'Computerizer/static/Blog/categories')
    title = models.CharField(max_length = 120)
    posts = models.ManyToManyField(Post)

    def __str__(self):
        return f'{self.title}'

class Sale(models.Model):
    image = models.ImageField(upload_to = r'Computerizer/static/Blog/sales')
    part = models.CharField(max_length = 60)
    body = models.TextField()
    link = models.URLField()

    def __str__(self):
        return f'{self.part}'
class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None)    
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.user}({self.post.title}): {self.body}'


class LikePost(models.Model):
    like_choices = [
        ('Liked', 'liked'),
        ('Disliked', 'disliked')
    ]

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like_state = models.CharField(choices=like_choices, max_length=15)
    user = models.ForeignKey(CustomUser, on_delete= models.CASCADE)

    def __str__(self):
        return f'{self.post.title}: {self.user}'

class LikeComment(models.Model):

    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)  
    user = models.ForeignKey(CustomUser, on_delete= models.CASCADE)

    def __str__(self):
        return f'{self.user}: {self.comment.body}'    
