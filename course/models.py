from django.db import models
from users.models import NULLABLE


class Course(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    imagine = models.ImageField(upload_to='courses/', verbose_name='Изображение', **NULLABLE)
    description = models.TextField(verbose_name='Описание')



