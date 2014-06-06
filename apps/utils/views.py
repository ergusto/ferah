from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import REDIRECT_FIELD_NAME, authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.debug import sensitive_post_parameters

from braces.views import LoginRequiredMixin, AjaxResponseMixin, AnonymousRequiredMixin

from apps.conversations.models import Message
from apps.conversations.utils.serializers import PaginatedMessageSerializer, MessageSerializer, ConversationSerializer, PaginatedConversationSerializer

from apps.utils.http import JSONResponse

# Create your views here.

class LoginView(AnonymousRequiredMixin, FormView):
    form_class = AuthenticationForm
    template_name = 'login/login.html'
    authenticated_redirect_url = u"/"

    def dispatch(self, *args, **kwargs):
        return super(LoginView, self).dispatch(*args, **kwargs)
 
    def form_valid(self, form):
        login(self.request, form.get_user())
        if self.request.is_ajax():
        	context = {
        		'redirect_url': reverse('home'),
        	}
        	return JSONResponse(context, status=200)
        return HttpResponseRedirect(reverse('home'))

    def form_invalid(self, form):
        self.set_test_cookie()
        if self.request.is_ajax():
        	return JSONResponse(form.errors, status=400)
        return super(LoginView, self).form_invalid(form)
 
    def set_test_cookie(self):
        self.request.session.set_test_cookie()
 
    def check_and_delete_test_cookie(self):
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()
            return True
        return False
 
    def get(self, request, *args, **kwargs):
        self.set_test_cookie()
        return super(LoginView, self).get(request, *args, **kwargs)
 
    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            self.check_and_delete_test_cookie()
            return self.form_valid(form)
        else:
            self.set_test_cookie()
            return self.form_invalid(form)

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