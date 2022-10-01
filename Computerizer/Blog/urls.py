from django.urls import path
from . import views

urlpatterns = [
    path('authors', views.getAuthors, name='author-api'),
    #-------------------------------
    path('recent-posts/', views.getRecentPosts, name='RecentPost-api'),
    path('post/<str:title>', views.getPost, name='post-api'),
    #-------------------------------
    path("post/like/", views.likePost, name='likePost-api'),
    path('post/likes/<str:title>', views.getPostLikes, name = 'postlikes-api'),
    path("post/unlike/", views.unlikePost, name='unlikePost-api'),
    #-------------------------------
    path('post/dislike/', views.dislikePost, name='dislikePost-api'),
    path('post/dislikes/<str:title>', views.getPostDislikes, name = 'postDislikes-api'),
    path('post/undislike/', views.undislikePost, name = 'undislikePost-api'),
    #-------------------------------
    path("comments/<str:post_title>", views.getComments, name='comments-api'),
    path('comment/create', views.createComment, name='createComment-api'),    
    path("comment/like/", views.likeComment, name='likeComment-api'),
    path("comment/unlike/", views.unlikeComment, name='unlikeComment-api'),
    path('comment/likes/<int:id>', views.getCommentLikes, name='getCommentLikes-api')
]