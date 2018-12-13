from django.shortcuts import render, redirect
from apps.posts.models import Post
from apps.users.models import User
from apps.comments.models import Comment
# Create your views here.
def index(request):
    if 'user_id' not in request.session:
        return redirect('users:login')
    else:
        userid = request.session['user_id']
        user = User.objects.filter(id=userid)
        for info in user:
            f_name = info.f_name.capitalize()

        post = Post.objects.all()
        comments = Comment.objects.all()
        context = {
            'user_id':userid,
            'all_post':post,
            'user_info':user,
            'name':f_name,
            'posts':post,
            'comments':comments

        }
        return render(request, 'posts/index.html', context)

def process_post(request):
    Post.objects.process_post(request.POST, request.session['user_id'])
    return redirect('posts:index')

def posts(request):
    return render(request, 'posts/posts.html')