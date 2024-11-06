





from django.contrib import admin
from django.urls import path
from users import views


app_name = 'users'

urlpatterns = [
   path('auth/', views.auth_form, name='auth'),
   path('login/', views.login, name='login'),
   path('logout/', views.logout, name='logout'),
   path('register/', views.register_form, name='register'),
   path('regestration/', views.regestration, name='regestration'),
   path('profile/', views.profile, name='profile'),
    
]

