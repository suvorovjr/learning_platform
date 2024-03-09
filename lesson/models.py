from django.db import models
from course.models import Course

NULLABLE = {'null': True, 'blank': True}


class Lesson(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    imagine = models.ImageField(upload_to='courses/', verbose_name='Изображение', **NULLABLE)
    description = models.TextField(verbose_name='Описание')
    video_link = models.URLField(verbose_name='Ссылка на видео', **NULLABLE)
    course = models.ForeignKey(Course, models.CASCADE, related_name='lesson', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
