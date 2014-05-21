from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from ..models import Conversation, Message
from serializers import ConversationSerializer, MessageSerializer
from permissions import IsOwnerOrReadOnly

class ConversationViewSet(ModelViewSet):
	queryset = Conversation.objects.all()
	serializer_class = ConversationSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

	def pre_save(self, obj):
		obj.user = self.request.user

class MessageViewSet(ModelViewSet):
	queryset = Message.objects.all()
	serializer_class = MessageSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)