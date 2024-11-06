from django.db import models

# Create your models here.


class Comment(models.Model):
    post=models.ForeignKey(to="posts.Post", on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    author = models.ForeignKey(to="users.User", on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text