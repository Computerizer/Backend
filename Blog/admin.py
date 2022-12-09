from django.contrib import admin
from .models import Post, Author, Comment, LikeComment, LikePost, Sale, Category


# Register your models here.
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(LikeComment)
admin.site.register(LikePost)
admin.site.register(Sale)
admin.site.register(Category)

