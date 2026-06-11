from rest_framework import permissions
from rest_framework.permissions import BasePermission


class ArticleOwnerPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.author