from django.urls import path
from article import views

app_name = 'article'
urlpatterns = [
    path('', views.article, name='article'),
    path('articleCreate/', views.articleCreate, name='articleCreate'),
    path('articleRead/<int:articleId>/', views.articleRead, name='articleRead'),
    path('articleUpdate/<int:articleId>/',views.articleUpdate, name='articleUpdate'),
    path('articleDelete/<int:articleId>/', views.articleDelete, name='articleDelete'),
    path('articleSearch/', views.articleSearch, name='articleSearch'),
    path('articleLike/<int:articleId>/', views.articleLike, name='articleLike'),
    path('commentCreate/<int:articleId>/', views.commentCreate, name='commentCreate'),
    path('commentUpdate/<int:commentId>/', views.commentUpdate, name='commentUpdate'),
    path('commentDelete/<int:commentId>/', views.commentDelete, name='commentDelete'),
]