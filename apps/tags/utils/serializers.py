from rest_framework import serializers

from ..models import Tag

class TagSerializer(serializers.ModelSerializer):
	get_absolute_url = serializers.CharField(source="get_absolute_url", read_only=True)

	class Meta:
		model = Tag
		fields = ('title', 'slug', 'get_absolute_url')