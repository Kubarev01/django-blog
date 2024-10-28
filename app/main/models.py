from django.db import models

# Create your models here.


class Blog(models.Model):
    slug=models.SlugField()
    title = models.CharField(max_length=50)
    content = models.TextField()
    description = models.CharField(max_length=100)
    made_by = models.CharField(max_length=20)
    picture = models.ImageField(upload_to='images/')
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.title} by {self.made_by}'
    
    