from rest_framework import serializers
from rest_framework.pagination import PaginationSerializer

from ..models import Tag

class TagSerializer(serializers.ModelSerializer):
	get_absolute_url = serializers.CharField(source="get_absolute_url", read_only=True)

	class Meta:
		model = Tag
		fields = ('title', 'slug', 'get_absolute_url')

class PaginatedTagSerializer(PaginationSerializer):

	class Meta:
		object_serializer_class = TagSerializer