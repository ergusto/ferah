from rest_framework import serializers
from rest_framework.pagination import PaginationSerializer

from apps.conversations.models import Message, Conversation

class MessageSerializer(serializers.ModelSerializer):
	get_absolute_url = serializers.CharField(source='get_absolute_url', read_only=True)
	user = serializers.RelatedField()
	date = serializers.DateTimeField(format='%B %d, %Y, %I:%M %p')
	conversation_absolute_url = serializers.CharField(source='conversation.get_absolute_url', read_only=True)
	conversation_title = serializers.CharField(source='conversation.title', read_only=True)
	get_edit_url = serializers.Field(source='get_edit_url')

	class Meta:
		model = Message
		fields = ('user', 'text', 'date', 'conversation_absolute_url', 'conversation_title', 'get_edit_url')

class PaginatedMessageSerializer(PaginationSerializer):

	class Meta:
		object_serializer_class = MessageSerializer

class ConversationSerializer(serializers.ModelSerializer):
	get_absolute_url = serializers.CharField(source='get_absolute_url', read_only=True)
	created = serializers.DateTimeField(format='%B %d, %Y, %I:%M %p')

	class Meta:
		model = Conversation
		fields = ('title', 'created', 'get_absolute_url', 'label')

class PaginatedConversationSerializer(PaginationSerializer):

	class Meta:
		object_serializer_class = ConversationSerializer