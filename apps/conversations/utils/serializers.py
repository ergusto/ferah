from rest_framework import serializers
from rest_framework.pagination import PaginationSerializer

from apps.conversations.models import Message, Conversation

class MessageSerializer(serializers.ModelSerializer):
	get_absolute_url = serializers.CharField(source='get_absolute_url', read_only=True)
	user = serializers.RelatedField()
	date = serializers.DateTimeField(format='%B %d, %Y, %I:%M %p')
	conversation_absolute_url = serializers.CharField(source='conversation.get_absolute_url', read_only=True)
	conversation_title = serializers.CharField(source='conversation.title', read_only=True)

	class Meta:
		model = Message
		fields = ('user', 'text', 'date', 'conversation_absolute_url', 'conversation_title')

class PaginatedMessageSerializer(PaginationSerializer):

	class Meta:
		object_serializer_class = MessageSerializer

class ConversationSerializer(serializers.ModelSerializer):
	get_absolute_url = serializers.CharField(source='get_absolute_url', read_only=True)
	created = serializers.DateTimeField(format='%B %d, %Y, %I:%M %p')
	get_label_display = serializers.CharField(source='get_label_display', read_only=True)

	class Meta:
		model = Conversation
		fields = ('title', 'created', 'get_absolute_url', 'get_label_display')

class PaginatedConversationSerializer(PaginationSerializer):

	class Meta:
		object_serializer_class = ConversationSerializer