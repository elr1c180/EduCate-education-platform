from django.db import models
from django.contrib.auth.models import AbstractUser

class Schools(models.Model):
    name = models.CharField(verbose_name='Название школы', max_length=200)

    class Meta:
        verbose_name = 'Школа'
        verbose_name_plural = 'Школы'
    
    def __str__(self) -> str:
        return self.name
    

class CustomUser(AbstractUser):
    surname = models.CharField(verbose_name='Отчество:', max_length=250, blank=True, null=True)
    school = models.ForeignKey('Schools', on_delete=models.CASCADE, verbose_name='Относится к школе:', blank=True, null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
    
    def __str__(self):
        return self.username