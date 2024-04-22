from django.db import models
from lesson.models import Lesson
from course.models import Course
from django.contrib.auth.models import AbstractUser

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='E-mail')
    phone = models.CharField(max_length=30, verbose_name='Телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Изображение', **NULLABLE)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Payment(models.Model):
    PAYMENT_METHODS = (
        ('by_card', 'Картой'),
        ('in_cash', 'Наличными'),
        ('transfer', 'Перевод'),
    )
    user = models.ForeignKey(User, models.CASCADE, verbose_name='Пользователь', related_name='payment', **NULLABLE)
    pay_data = models.DateField(auto_now_add=True, verbose_name='Дата оплаты')
    paid_course = models.ForeignKey(Course, models.CASCADE, verbose_name='Оплаченный курс', related_name='payment')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS, verbose_name='Способ оплаты')
    payment_status = models.BooleanField(default=False, verbose_name='Статус платежа')

    def __str__(self):
        return f'{self.user} - {self.paid_course}'

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
        ordering = ('-pay_data',)
