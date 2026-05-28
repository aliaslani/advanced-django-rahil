from django.urls import path
from apps.article.view import ArticleListAPIView, ArticleDetailAPIView

urlpatterns = [
    path('', ArticleListAPIView.as_view(), name='article-list'),
    path('<int:pk>/', ArticleDetailAPIView.as_view(), name='article-detail'),

]