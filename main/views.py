from django.shortcuts import render
from posts.models import Post

def index(request):
    
   
    context={
        'title':'black+:Главная',
        
    }

    return render(request,'main/Index.html',context)


def show_detail_post(request,post_slug):
    
    post=Post.objects.get(slug=post_slug)
    context={
        'post':post
    }

    return render(request,'main/blog.html',context)


def about(request):
    context={
        'title':'black+:О нас',
    }

    return render(request,'main/about-us.html',context)