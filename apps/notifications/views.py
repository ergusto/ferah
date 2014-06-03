from django.views.generic.list import ListView
from django.views.generic.base import RedirectView

from braces.views import LoginRequiredMixin, AjaxResponseMixin

from models import Notification

# Create your views here.

class NotificationListView(LoginRequiredMixin, ListView):
	model = Notification
	paginate_by = 20

	def get_queryset(self):
		return self.request.user.profile.unread_notifications()

class NotificationRedirectView(LoginRequiredMixin, RedirectView):
	permanent = False

	def get_object(self):
		return Notification.objects.get(id=self.kwargs['pk'])

	def dispatch(self, request, *args, **kwargs):
		self.object = self.get_object()
		if self.object.user != self.request.user:
			return HttpResponseRedirect(reverse_lazy('home'))
		return super(NotificationRedirectView, self).dispatch(request, *args, **kwargs)

	def get_redirect_url(self, *args, **kwargs):
		object = self.get_object()
		object.read = True
		object.save()
		return object.content_object.conversation.get_absolute_url()