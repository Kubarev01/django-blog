from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    
    email = models.EmailField(unique=True, blank=True,null=True,verbose_name='Электронная почта')
    
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='Обновлен')

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['id']
        