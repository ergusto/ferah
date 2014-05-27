from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from braces.views import LoginRequiredMixin, AjaxResponseMixin

from apps.conversations.models import Message
from apps.conversations.utils.serializers import PaginatedMessageSerializer, MessageSerializer, ConversationSerializer, PaginatedConversationSerializer

from apps.utils.http import JSONResponse

# Create your views here.

class UtilsView(LoginRequiredMixin, TemplateView):
	template_name = 'utils/utils.html'

class UserMessagesView(LoginRequiredMixin, AjaxResponseMixin, ListView):
	model = Message
	template_name = 'utils/user.html'
	paginate_by = 10

	def get_queryset(self):
		return self.request.user.messages.all().order_by('-date')

	def get_ajax(self, request, *args, **kwargs):
		self.object_list = self.get_queryset()
		paginator = Paginator(self.object_list, 10)
		page = request.GET.get('page', '')
		try:
			queryset = paginator.page(page)
		except PageNotAnInteger:
			queryset = paginator.page(1)
		except EmptyPage:
			queryset = paginator.page(paginator.num_pages)
		serializer_context = {'request': request}
		serializer = PaginatedMessageSerializer(queryset, context=serializer_context)
		return JSONResponse(serializer.data, status=200)