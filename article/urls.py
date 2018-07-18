from django.urls import path
from article import views

app_name = 'article'
urlpatterns = [
    path('', views.article, name='article'),
]