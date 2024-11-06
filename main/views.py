from django.shortcuts import render
from comments.models import Comment
from posts.models import Post

def index(request):
    
   
    context={
        'title':'black+:Главная',
        
    }

    return render(request,'main/Index.html',context)


def show_detail_post(request,post_slug):
    
    comments=Comment.objects.filter(post__slug=post_slug)
    post=Post.objects.get(slug=post_slug)
    context={
        'post':post,
        'comments':comments
    }

    return render(request,'main/blog.html',context)


def about(request):
    context={
        'title':'black+:О нас',
    }

    return render(request,'main/about-us.html',context)