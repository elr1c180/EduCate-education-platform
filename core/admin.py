from django.contrib import admin
from .models import Questions, Answers, Tests, EducationArticles

class TestList(admin.ModelAdmin):
    list_display = ('title', 'level')
    search_field = ('title')

admin.site.register(Tests, TestList)

class AnswersList(admin.ModelAdmin):
    list_display = ('title', 'is_true', 'question')
    search_field = ('title')

admin.site.register(Answers,AnswersList)

admin.site.register(Questions)
admin.site.register(EducationArticles)