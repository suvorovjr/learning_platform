from django.db import models
from users.models import NULLABLE


class Lesson(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    imagine = models.ImageField(upload_to='courses/', verbose_name='Изображение', **NULLABLE)
    description = models.TextField(verbose_name='Описание')
    video_link = models.URLField(verbose_name='Ссылка на видео', **NULLABLE)
