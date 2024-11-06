


from django.contrib import admin
from django.urls import path
from comments import views


app_name = 'comments'

urlpatterns = [
   path('leave_a_comment/<slug:post_slug>/', views.leave_comment, name='leave_a_comment'),
   
]

