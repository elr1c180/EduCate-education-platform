from django.contrib import admin
from .models import Schools, CustomUser

admin.site.register(Schools)

class User(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'surname', 'school', 'email')
admin.site.register(CustomUser, User)