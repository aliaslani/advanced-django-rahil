from django.contrib import admin
from apps.article.models import Article, Tag

admin.site.register(Tag)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('author',)
    list_display = ('title', 'author')


