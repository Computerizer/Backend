from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.getCategories, name='categories-api'),
    #-------------------------------
    path('recent-posts/<int:num_of_posts>/<int:page_num>', views.getRecentPosts, name='RecentPost-api'),
    path('post/<str:title>', views.getPost, name='post-api'),
    path('post/view/', views.viewPost, name='viewPost-api'),
    #-------------------------------
    path("post/like/", views.LikePostView.as_view(), name='likePost-api'),
    #-------------------------------
    path('post/dislike/', views.DislikePost.as_view(), name='dislikePost-api'),
    #-------------------------------
    path("comments/<str:post_title>", views.getComments, name='comments-api'),
    path('comment/create', views.CreateComment.as_view(), name='createComment-api'),    
    path("comment/like/", views.LikeCommentView.as_view(), name='likeComment-api'),
    #-------------------------------
    path('search/<str:query>', views.searchBlog, name='searchBlog-api'),

    path('test/tinymce', views.test1, name='Tinymcetest')

    #------------------------------

]