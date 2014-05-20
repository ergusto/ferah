from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from braces.views import LoginRequiredMixin, AjaxResponseMixin

from apps.conversations.models import Conversation
from apps.conversations.utils.serializers import PaginatedConversationSerializer
from apps.utils.http import JSONResponse

class HomeView(LoginRequiredMixin, AjaxResponseMixin, ListView):
	template_name = 'home/home.html'
	paginate_by = 10

	def get_queryset(self):
		return Conversation.objects.all().order_by('-last_activity')

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
		serializer = PaginatedConversationSerializer(queryset, context=serializer_context)
		return JSONResponse(serializer.data, status=200)