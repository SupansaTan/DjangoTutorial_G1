from django.urls import path

from . import views

app_name = 'vocab'
urlpatterns = [
    path('', views.index, name='index'),
    path('<form/', views.detail, name='detail'),
    path('add/', views.addvocab, name='add'),
]