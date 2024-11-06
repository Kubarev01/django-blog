from django.contrib import admin
from django.urls import path
from main import views

app_name='main'

urlpatterns = [
    path('', views.index,name='index'),
    path('about/', views.about,name='about'),
    path('post/<slug:post_slug>', views.show_detail_post, name='post'),
]


