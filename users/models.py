from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='E-mail')
    phone = models.CharField(max_length=30, verbose_name='Телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Изображение', **NULLABLE)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
