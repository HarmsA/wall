from django.shortcuts import render, redirect
from django.contrib import messages

from apps.users.models import User

# Create your views here.
def login(request):
    return render(request, 'users/login.html')

def login_validate(request):
    if User.objects.login_validate(request.POST):
        request.session['user_id'] = User.objects.get(email=request.POST['email']).id
        print(User.objects.get(email=request.POST['email']).id)
        return redirect('posts:index')
    else:
        error = "Email or Password is invalid"
        messages.error(request, error)
        return redirect('users:login')

def register(request):
    return render(request, 'users/register.html')


def register_validate(request):
    errors = User.objects.register_validate(request.POST)
    if errors:
        for error in errors:
            messages.error(request, error)
    else:
        user = User.objects.create_user(request.POST)
        request.session['user_id'] = user.id
        return redirect('posts:index')
    return redirect('users:register')

def logout(request):
    request.session.clear()
    return redirect('users:login')