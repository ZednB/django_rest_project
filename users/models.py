from django.db import models

from django.contrib.auth.models import AbstractUser

from materials.models import Course, Lesson

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    phone = models.CharField(max_length=35, verbose_name='Номер телефона', **NULLABLE)
    city = models.CharField(max_length=150, verbose_name='Город', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email} - {self.phone}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'


class Payment(models.Model):
    CHOICES = [
        ('cash', 'Наличный'),
        ('transfer', 'Перевод')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    payment_date = models.DateTimeField(verbose_name='Дата оплаты', **NULLABLE)
    payed_course = models.ManyToManyField(Course, verbose_name='Оплаченный курс', **NULLABLE),
    payed_lesson = models.ManyToManyField(Lesson, verbose_name='Оплаченный урок', **NULLABLE)
    amount = models.PositiveIntegerField(verbose_name='Сумма оплаты')
    method = models.CharField(choices=CHOICES, max_length=15, verbose_name='Способ оплаты')

    def __str__(self):
        return f'{self.user} - {self.amount}, {self.method}'

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
