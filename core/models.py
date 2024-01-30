from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

LEVEL = {
    "B":"Базовый",
    "A":"Углубленный"
}

class Questions(models.Model):
    title = models.CharField(verbose_name='Название вопроса:', max_length=250)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
    
    def __str__(self) -> str:
        return self.title

class Answers(models.Model):
    title = models.CharField(verbose_name='Ответ:', max_length=250)
    is_true = models.BooleanField(verbose_name='Отметить, если это правильный ответ:')
    question = models.ForeignKey('Questions', on_delete=models.CASCADE, verbose_name='Прикрепить к вопросу:')

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
    
    def __str__(self) -> str:
        return self.title


class Tests(models.Model):
    title = models.CharField(verbose_name='Название теста:', max_length=550)
    questions = models.ManyToManyField('Questions', verbose_name='Выберите вопросы для теста:')
    level = models.CharField(verbose_name='Уровень теста', max_length=250, choices=LEVEL)

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'
    
    def __str__(self) -> str:
        return self.title
    
class EducationArticles(models.Model):
    title = models.CharField(verbose_name='Заголовок обучающего блока:', max_length=550)
    text = CKEditor5Field('Полный текст:')

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = "Материалы"
    
    def __str__(self):
        return self.title