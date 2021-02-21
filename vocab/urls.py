from django.urls import path

from . import views

app_name = 'vocab'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:vocabs_id>/', views.detail, name='detail'),
]