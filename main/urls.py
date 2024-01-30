from django.urls import path, include
from .views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('', main, name='main_page'),
    path('reg/',  reg, name='reg_page'),
    path('profile/', include('django.contrib.auth.urls'))
]