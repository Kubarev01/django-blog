from django.contrib import admin
from posts.models import Post

# Register your models here.

@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}
    list_display=["title"]
