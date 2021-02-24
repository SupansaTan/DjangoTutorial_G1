from django.urls import path

from . import views

app_name = 'vocab'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:vocab_id>/', views.detail, name='detail'),
    path('add/', views.addVocab, name='add'),
    path('result/', views.search, name='search'),
    path('delete/<int:vocab_id>/', views.deleteVocab, name='delete')
]