from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib import messages,auth
from django.urls import reverse
from posts.models import Post
from users.forms import UserSignUpForm,UserRegisterForm
# Create your views here.



def logout(request):
    return render(request,'users/logout.html')



def register_form(request):
    return render(request,'users/reg.html')


def regestration(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            
            user= form.instance
            auth.login(request,user)
            messages.success(request,f"{user.username}, вы успешно зарегистрировались!")
            return HttpResponseRedirect(reverse('users:profile'))

    else:
        form = UserRegisterForm()
        messages.error(request,'Неправильный логин или пароль!')
    context={
            'title':'Home - Регистрация',
            'form':form
        }
    return render(request,'users/reg.html',context)


def auth_form(request):
    return render(request,'users/auth.html')


@login_required
def profile(request):
    
    posts=Post.objects.filter(made_by=request.user)
    context={
        'title':'Home - Профиль',
        'user': request.user,
        'posts':posts
    }

    
    return render(request,'users/profile.html',context)


def login(request):
    if request.method == 'POST':
        form = UserSignUpForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                auth.login(request,user)
                messages.success(request,f"{user.username}, вы успешно авторизовались!")
                return HttpResponseRedirect(reverse('users:profile'))

    else:
        form = UserSignUpForm()
        messages.error(request,'Неправильный логин или пароль!')
    context={
                'title':'Home - Авторизация',
                'form':form
            }
    return render(request,'users/auth.html',context)


def add_new_post(request):
    return render(request,'users/add_new_post.html')



@login_required()
def logout(request):
   
   auth.logout(request)
   return redirect('main:index')