from rest_framework import serializers
from rest_framework.pagination import PaginationSerializer

from apps.conversations.models import Message, Conversation

class MessageSerializer(serializers.ModelSerializer):
	get_absolute_url = serializers.CharField(source='get_absolute_url', read_only=True)
	user = serializers.RelatedField()
	date = serializers.DateTimeField(format='%B %d, %Y, %I:%M, %p')

	class Meta:
		model = Message
		fields = ('user', 'text', 'date')

class PaginatedMessageSerializer(PaginationSerializer):

	class Meta:
		object_serializer_class = MessageSerializer

class ConversationSerializer(serializers.ModelSerializer):
	get_absolute_url = serializers.CharField(source='get_absolute_url', read_only=True)
	created = serializers.DateTimeField(format='%B %d, %Y, %I:%M, %p')

	class Meta:
		model = Conversation
		fields = ('title', 'created')

class PaginatedConversationSerializer(PaginationSerializer):

	class Meta:
		object_serializer_class = ConversationSerializer