from django.db import models

from django.contrib.auth.models import AbstractUser

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    phone = models.CharField(max_length=35, verbose_name='Номер телефона', **NULLABLE)
    city = models.CharField(max_length=150, verbose_name='Город', **NULLABLE)
    avaatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email} - {self.phone}'

    class Meta:
        permissions = [
            ('view_all_users', 'Can view all users'),
            ('block_user', 'Can block users'),
        ]
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
