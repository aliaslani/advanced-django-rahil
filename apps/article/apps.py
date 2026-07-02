from django.apps import AppConfig


class ArticleConfig(AppConfig):
    name = 'apps.article'

    def ready(self):
        import apps.article.signals

