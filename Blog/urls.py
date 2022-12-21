from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.getCategories, name='categories-api'),
    #-------------------------------
    path('sales/<int:num_of_sales>', views.getSales, name='sales-api'),
    #-------------------------------
    path('recent-posts/<int:num_of_posts>/<int:page_num>', views.getRecentPosts, name='RecentPost-api'),
    path('posts/<str:order>/<int:num_of_posts>', views.getPostsOrdered, name='PostOrder-api'),
    path('post/<str:title>', views.getPost, name='post-api'),
    path('post/view/', views.viewPost, name='viewPost-api'),
    #-------------------------------
    path("post/like/", views.LikePostView.as_view(), name='likePost-api'),
    path('post/likes/<str:title>', views.getPostLikes, name = 'postlikes-api'),
    path("post/unlike/", views.UnlikePost.as_view(), name='unlikePost-api'),
    #-------------------------------
    path('post/dislike/', views.DislikePost.as_view(), name='dislikePost-api'),
    path('post/dislikes/<str:title>', views.getPostDislikes, name = 'postDislikes-api'),
    path('post/undislike/', views.UndislikePost.as_view(), name = 'undislikePost-api'),
    #-------------------------------
    path("comments/<str:post_title>", views.getComments, name='comments-api'),
    path('comment/create', views.CreateComment.as_view(), name='createComment-api'),    
    path("comment/like/", views.LikeCommentView.as_view(), name='likeComment-api'),
    path("comment/unlike/", views.UnlikeComment.as_view(), name='unlikeComment-api'),
    path('comment/likes/<int:id>', views.getCommentLikes, name='getCommentLikes-api'),
    #-------------------------------
    path('search/<str:query>', views.searchBlog, name='searchBlog-api'),

    #------------------------------

]