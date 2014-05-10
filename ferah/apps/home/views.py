from django.views.generic import TemplateView

from braces.views import LoginRequiredMixin

from apps.conversations.models import Conversation

class HomeView(LoginRequiredMixin, TemplateView):
	template_name = 'home/home.html'

	def get_context_data(self, **kwargs):
		context = super(HomeView, self).get_context_data(**kwargs)
		context['conversations'] = Conversation.objects.all()
		return context