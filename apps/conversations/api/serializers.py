from rest_framework import serializers

from ..models import Conversation, Message

class MessageSerializer(serializers.HyperlinkedModelSerializer):
	user = serializers.Field(source='user.username')
	conversation = serializers.HyperlinkedRelatedField(view_name='conversation-detail')
	get_edit_url = serializers.Field(source='get_edit_url')

	class Meta:
		model = Message
		fields = ('id', 'user', 'conversation', 'text', 'date', 'get_edit_url')

class ConversationSerializer(serializers.HyperlinkedModelSerializer):
	user = serializers.Field(source='user.username')
	messages = serializers.HyperlinkedRelatedField(view_name='message-detail', many=True)
	get_absolute_url = serializers.Field(source='get_absolute_url')

	class Meta:
		model = Conversation
		fields = ('id', 'user', 'title', 'slug', 'label', 'created', 'last_activity', 'get_absolute_url', 'messages')