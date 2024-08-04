from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('article/', views.article_list, name='article'),
]