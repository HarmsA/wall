from django.shortcuts import render, redirect
from apps.comments.models import Comment
from django.contrib import messages


# Create your views here.
def process(request):
    errors = Comment.objects.verify_comment(request.POST)
    if errors:
        for error in errors:
            messages.error(request, error)
    else:
        user_id = request.session['user_id']
        print(user_id)
        print('9'*80)
        Comment.objects.create_comment(request.POST, user_id)
    return redirect('posts:index')