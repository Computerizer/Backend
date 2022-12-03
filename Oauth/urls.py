from django.urls import path
from rest_framework.authtoken import views
from .views import *
urlpatterns = [
    path('api/users/create-user',post_view,name='post_view'),
    path('api/user',get_current_user_info,name='get_view'),
    path('api/users/update-info',update_user_information,name='update_user_info'),
    path('api/users',get_all_users_info,name='all_users'),
    path('api/users/delete-user',delete_user,name='delete_user'),
    path('api-token-auth', views.obtain_auth_token,name='auth_token')
]