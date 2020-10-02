from rest_framework import serializers

from core.models import TAGS_URL


class TagSerializer(serializer.ModelSerializer):
    """Tag for the tag object"""

    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id',)
