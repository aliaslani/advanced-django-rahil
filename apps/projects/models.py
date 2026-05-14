from django.db import models
from apps.users.models import User
from apps.organizations.models import Organization
from apps.core.models import BaseModel


class Project(BaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField()
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='projects', blank=True)
    status = models.CharField(max_length=200, choices=[('in_progress', 'inprogress'), ('pending', 'pending')], default='pending')
    deadline = models.DateTimeField(null=True, blank=True)


    class Meta:
        verbose_name = 'پروژه'
        verbose_name_plural = 'پروژه'

    def __str__(self):
        return self.name


class Task(BaseModel):
    PRIORITY_CHOICES = [
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
        (4, 'Critical'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks')
    reporter = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True, related_name='reports')
    priority = models.IntegerField(default=0, choices=PRIORITY_CHOICES)
    is_done = models.BooleanField(default=False)
    due_date = models.DateTimeField(null=True, blank=True)
    estimated_hours = models.DecimalField(max_digits=5, decimal_places=2)
    tags = models.JSONField(default=list, blank=True)
    class Meta:
        verbose_name = 'تسک'
        verbose_name_plural = 'تسک'

    def __str__(self):
        return self.title

class Comment(BaseModel):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='comments')
    body = models.TextField()


    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت'

    def __str__(self):
        return f'{self.body[:100]} ...'







