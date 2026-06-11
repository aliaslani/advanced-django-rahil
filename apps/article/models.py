from django.db import models
from apps.users.models import User
from apps.core.models import BaseModel

class Tag(BaseModel):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Article(BaseModel):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
