from sqlite3 import IntegrityError
from django.shortcuts import render
from rest_framework.response import Response
from Oauth.models import CustomUser
from .models import Author, Post, Post_Image, Comment,Category
from .serializer import AuthorSerializer, ImagePostSerializer, PostSerializer, RecentPostSerializer, CommentSerializer, CategorySerializer
from django.core.files.storage import default_storage
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly,AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.views import APIView
from django.db.models import Q
from django.core.paginator import Paginator


@api_view(['GET'])
def getCategories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many = True)

    posts = []
    for category in serializer.data:
        for postId in category["posts"]:
            post = Post.objects.get(id = postId)
            posts += [post.title]
        category['posts'] = posts
        posts = []      
        
    return Response(serializer.data)

@api_view(["GET"])
def getRecentPosts(request, num_of_posts, page_num):
    posts = Post.objects.filter(status = 'Published').order_by('-publish_date')
    objects = Paginator(posts, num_of_posts)
    if page_num <= len(objects.page_range):
        serializer = RecentPostSerializer(objects.page(page_num), many=True)
        
        for post in serializer.data:
            cureent_post = Post.objects.get(id = post["id"])
            post['post_url'] = cureent_post.get_absolute_url()
            post['author'] = cureent_post.author.name
            post['likes'] = cureent_post.get_likes_num()
            post['dislikes'] = cureent_post.get_dislikes_num()

        return Response(serializer.data)
    else:
        return Response('Out of range')        



@api_view(["GET"])
def getPost(request, title):
    post = Post.objects.get(title = title)
    images = Post_Image.objects.filter(post = post)
    image_serializer = ImagePostSerializer(images, many = True)

    serializer = PostSerializer(post)
    f = default_storage.open(str(post.body))
    body = f.read().decode("utf-8")

    # replacing image title in html to image link
    for image in image_serializer.data:
        # [] inside f'' not working
        photo = image['title']
        index = body.find(f'src="{photo}"')
        
        # checking if image src in the file( index = -1 means not found)
        if index != -1:
            image = image['image']
            body = body.replace(body[index : index + len(f"src='{photo}'")] , f'src="{image}"')
        else:
            # checking if there src = '' instead of src = ""
            index = body.find(f"src='{photo}'") 
            if index != -1:
                image = image['image']
                body = body.replace(body[index : index + len(f"src='{photo}'")] , f"src='{image}'") 
            

    data = {
            'title': post.title,
            'author' : post.author.name,
            'body' : body,
            'description' : post.description,
            'image': serializer.data['image'],
            'publish_date': post.publish_date,
            'likes' : post.get_likes_num(),
            'dislikes' : post.get_dislikes_num(),
            'views' : post.views,
            'categories' : []
        }
    categories = Category.objects.filter(posts = post)
    for categorie in categories:
        data['categories'].append(categorie.title)

    return Response(data, status=200)



@api_view(["POST"])
def viewPost(request):
    post = Post.objects.get(title = request.data['post'])

    post.views += 1
    post.save()
    return Response("Post Viewed")
    
@api_view(['GET'])
def getComments(request, post_title):
    post = Post.objects.get(title = post_title)
    comments = Comment.objects.filter(post = post)
    serializer = CommentSerializer(comments, many = True)
    for i in serializer.data:
        user = CustomUser.objects.get(id = i['user'])
        comment = Comment.objects.get(id = i['id'])
        i['user'] = user.username
        i['post'] = post.title
        i['likes'] = comment.get_likes_num()
        
    return Response(serializer.data)


class CreateComment(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self ,request):
        post = Post.objects.get(title = request.data['post'])
        user = CustomUser.objects.get(username= request.data['user'])
        if user == request.user:
            data = {
                'body' : request.data['body'],
                'user' : user.id,
                'post' : post.id
            }
            serializer = CommentSerializer(data= data)
            if serializer.is_valid():
                serializer.save()
                return Response('success')
            else:
                return Response('Not allowed', status=400)  
        else:
            return Response("You don't have permission to do this", status=401)


class LikePostView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        post = Post.objects.get(title = request.data['post'])
        user = request.user

        #check if already diliked or liked by user 
    
        if user in post.likes.all():
            post.likes.remove(user)

            post.save()
            return Response('post unliked')
        else:
            if user in post.dislikes.all():
                post.dislikes.remove(user)

            post.likes.add(user)
            
            post.save()
                
            return Response('post liked')



class DislikePost(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        post = Post.objects.get(title = request.data['post'])
        user = request.user

        
        #check if already disliked or liked by user 
        if user in post.dislikes.all():
            post.dislikes.remove(user)

            return Response('post undisliked')
        else:    
            if user in post.likes.all():
                post.likes.remove(user)

            post.dislikes.add(user)
            
            post.save()
            
            return Response('post disliked')




class LikeCommentView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        comment_user = CustomUser.objects.get(username = request.data['comment_user'])
        post = Post.objects.get(title = request.data['post'])

        comment = Comment.objects.get(body = request.data['body'], user = comment_user, post = post)
        user = request.user
        if user in comment.likes.all():
            comment.likes.remove(user)

            comment.save()

            return Response('comment unliked')
        else:
            comment.likes.add(user)

            comment.save()    

            return Response('comment liked')


 



@api_view(["GET"])
def searchBlog(request, query):
    posts = Post.objects.filter(Q(title__icontains = query) | Q(description__icontains = query))
    categories = Category.objects.filter(Q(title__icontains = query))

    serializer = RecentPostSerializer(posts, many = True)
    categoriesSerializer = CategorySerializer(categories, many = True)
    
    data = {}
    data['posts'] = serializer.data
    data['categories'] = categoriesSerializer.data
    
    return Response(data)