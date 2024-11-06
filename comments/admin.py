from django.contrib import admin

# Register your models here.
from comments.models import Comment

# Register your models here.

@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display=["text"]
