from django.template.context_processors import request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny, IsAdminUser
from rest_framework import status
from django.shortcuts import render, get_object_or_404
from apps.article.models import Article
from apps.article.serializers import ArticleSerializer, ArticleDetailSerializer
from rest_framework import generics
from apps.article.permissions import ArticleOwnerPermission
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

class ArticleListAPIView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ArticleDetailAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        serializer = ArticleSerializer(article, data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        serializer = ArticleSerializer(article, data=request.data, context={'request': request}, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class ArticleListCreateView(generics.ListCreateAPIView):
    serializer_class = ArticleSerializer
    pagination_class = None
    def get_queryset(self):
        return Article.objects.all()
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ArticleRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated, ArticleOwnerPermission]

    # def get_serializer_class(self):
    #     if request.method in( 'GET', 'PUT', 'PATCH'):
    #         return ArticleDetailSerializer
    #     else:
    #         return ArticleSerializer
    #
    # def perform_update(self, serializer):
    #     serializer.save(author=self.request.user)
    #
    # def perform_destroy(self, serializer):
    #     serializer.save(author=self.request.user)



class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [AllowAny]


    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def publish(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        article.is_published = True
        article.save()
        return Response(status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get'], url_path='published-articles')
    def published_articles(self, request):
        articles = Article.objects.filter(is_published=True)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



