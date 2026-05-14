from rest_framework import serializers

from apps.projects.models import Project


class ProjectStatSerializer(serializers.Serializer):
    project_id = serializers.IntegerField(read_only=True)
    project_name = serializers.CharField(read_only=True)
    total_tasks = serializers.IntegerField(read_only=True)
    completed_tasks = serializers.IntegerField(read_only=True)
    completed_percentage = serializers.FloatField(read_only=True)
    overdue_tasks = serializers.IntegerField(read_only=True)
    members_count = serializers.IntegerField(read_only=True)


class ProjectSerializer(serializers.ModelSerializer):
    tasks_count = serializers.IntegerField(source='tasks.count', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    name_of_reporter = serializers.SerializerMethodField(read_only=True)




    def get_name_of_reporter(self):
