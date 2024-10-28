from django.shortcuts import render

def index(request):
    context={
        'title':'black+:Главная',
    }

    return render(request,'main/Index.html',context)

def about(request):
    context={
        'title':'black+:О нас',
    }

    return render(request,'main/about-us.html',context)