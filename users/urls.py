from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('name/', views.homeView, name='name1'),
]