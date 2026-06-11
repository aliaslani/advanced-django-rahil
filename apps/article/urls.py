from django.urls import path
from apps.article.views import ArticleListAPIView, ArticleDetailAPIView, ArticleListCreateView, ArticleRetrieveUpdateDestroyAPIView, ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='articles')

urlpatterns = router.urls
urlpatterns += [
    # path('', ArticleListAPIView.as_view(), name='article-list'),
    # path('', ArticleListCreateView.as_view(), name='article-list'),
    # path('<str:pk>/', ArticleRetrieveUpdateDestroyAPIView.as_view(), name='article-detail'),



]