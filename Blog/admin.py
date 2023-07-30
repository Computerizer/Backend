from django.contrib import admin
from .models import Post, Post_Image, Author, Comment, Category


# Register your models here.
admin.site.register(Author)
admin.site.register(Comment)
# admin.site.register(LikeComment)
# admin.site.register(LikePost)
# admin.site.register(Sale)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Post_Image)

