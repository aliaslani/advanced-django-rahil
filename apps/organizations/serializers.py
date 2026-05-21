from rest_framework import serializers
from apps.organizations.models import Organization


class OrganizationHyperlinkedSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)
    projects_url = serializers.HyperlinkedIdentityField(view_name='project-detail', read_only=True, lookup_field='slug')
    members_url = serializers.HyperlinkedIdentityField(view_name='member-detail', read_only=True)
    class Meta:
        model = Organization
        fields = [
            'url',
            'name', 'slug', 'owner', 'members_url', 'plan','projects_url','created_at'
        ]
        extra_kwargs = {
            'url': {
                'view_name': 'organization-detail',
                'lookup_field': 'slug'
            }
        }

