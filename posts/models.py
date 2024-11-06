from django.db import models
from django.urls import reverse

from users.models import User
# Create your models here.

class Post(models.Model):
    slug=models.SlugField(max_length=200, unique=True,blank=True,null=True,verbose_name='URL')
    title = models.CharField(max_length=50,verbose_name='Заголовок')
    text = models.TextField(max_length=5000,verbose_name='Текст')
    description = models.CharField(blank=True,null=True,verbose_name='Описание')
    made_by = models.ForeignKey(to="users.User", blank=True, null=True, on_delete=models.CASCADE,verbose_name='Автор')
    image = models.ImageField(upload_to='posts_images',blank=True,null=True,verbose_name='Изображение')
    likes = models.IntegerField(default=0)
    # comments = models.ForeignKey(to=Comments, on_delete=models.CASCADE,blank=True,null=True,verbose_name='Комментарии')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table='posts'
        verbose_name='Пост'
        verbose_name_plural='Посты'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.title} by '  
    
    def get_absolute_url(self):
        return reverse("posts:post", kwargs={"post_slug": self.slug})
    
    