from rest_framework import serializers

from ..models import Conversation, Message

class MessageSerializer(serializers.HyperlinkedModelSerializer):
	user = serializers.Field(source='user.username')
	conversation = serializers.HyperlinkedRelatedField(view_name='conversation-detail')

	class Meta:
		model = Message
		fields = ('user', 'conversation', 'text', 'date')

class ConversationSerializer(serializers.HyperlinkedModelSerializer):
	user = serializers.Field(source='user.username')
	messages = serializers.HyperlinkedRelatedField(view_name='message-detail', many=True)
	get_absolute_url = serializers.Field(source='get_absolute_url')

	class Meta:
		model = Conversation
		fields = ('user', 'title', 'slug', 'label', 'created', 'last_activity', 'get_absolute_url', 'messages')