import csv
from datetime import date

from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, FormView, DetailView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from braces.views import LoginRequiredMixin, AjaxResponseMixin

from apps.utils.http import JSONResponse

from forms import ConversationForm, MessageForm
from models import Conversation, Message
from utils.serializers import PaginatedMessageSerializer, MessageSerializer, ConversationSerializer, PaginatedConversationSerializer

class ConversationListView(LoginRequiredMixin, ListView):
	model = Conversation
	paginate_by = 50
	template_name = 'conversations/list.html'

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

class ConversationFormView(LoginRequiredMixin, FormView):
	form_class = ConversationForm
	template_name = 'conversations/form.html'

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.user = self.request.user
		self.object.save()
		if self.request.is_ajax():
			serializer = ConversationSerializer(self.object)
			return JSONResponse(serializer.data, status=200)
		return HttpResponseRedirect(self.object.get_absolute_url())

	def form_invalid(self, form):
		if self.request.is_ajax():
			return JSONResponse(form.errors, status=400)
		return super(ConversationFormView, self).form_invalid(form)

class ConversationDeleteView(LoginRequiredMixin, DeleteView):
	model = Conversation
	success_url = reverse_lazy('home')

	def get_object(self, **kwargs):
		return Conversation.objects.get(slug=self.kwargs['slug'])

	def dispatch(self, request, *args, **kwargs):
		self.object = self.get_object()
		if not self.object.user == request.user:
			return HttpResponseRedirect(reverse_lazy('home'))
		return super(ConversationDeleteView, self).dispatch(request, *args, **kwargs)

class ConversationDetailView(LoginRequiredMixin, AjaxResponseMixin, ListView):
	template_name = 'conversations/detail.html'
	paginate_by = 10

	def get_object(self, **kwargs):
		return Conversation.objects.get(slug=self.kwargs['slug'])

	def get_queryset(self):
		object = self.get_object()
		return object.descending_messages()

	def get_context_data(self, **kwargs):
		context = super(ConversationDetailView, self).get_context_data(**kwargs)
		context['message_form'] = MessageForm()
		context['object'] = self.get_object()
		return context

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

class ConversationEditView(LoginRequiredMixin, AjaxResponseMixin, UpdateView):
	form_class = ConversationForm
	template_name = 'conversations/form.html'

	def get_object(self, **kwargs):
		return Conversation.objects.get(slug=self.kwargs['slug'])

	def form_valid(self, form):
		self.object = form.save()
		if self.request.is_ajax():
			serializer = ConversationSerializer(self.object)
			return JSONResponse(serializer.data, status=200)
		return HttpResponseRedirect(self.object.get_absolute_url())

	def form_invalid(self, form):
		if self.request.is_ajax():
			return JSONResponse(form.errors, status=400)
		return super(ConversationFormView, self).form_invalid(form)

	def dispatch(self, request, *args, **kwargs):
		object = self.get_object()
		if not object.user == request.user:
			return HttpResponseRedirect(reverse_lazy('home'))
		return super(ConversationEditView, self).dispatch(request, *args, **kwargs)

class ConversationMessageFormView(LoginRequiredMixin, FormView):
	form_class = MessageForm
	template_name = 'conversations/message_form.html'

	def get_object(self, **kwargs):
		return Conversation.objects.get(slug=self.kwargs['slug'])

	def get_success_url(self):
		object = self.get_object()
		return object.get_absolute_url()

	def form_valid(self, form):
		self.object = form.save(commit=False)
		conversation = self.get_object()
		self.object.user = self.request.user
		self.object.conversation = conversation
		self.object.save()
		if self.request.is_ajax():
			serializer = MessageSerializer(self.object)
			return JSONResponse(serializer.data, status=200)
		return HttpResponseRedirect(self.get_success_url())

	def form_invalid(self, form):
		if self.request.is_ajax():
			return JSONResponse(form.errors, status=400)
		return super(ConversationMessageFormView, self).form_invalid(form)

	def get_context_data(self, **kwargs):
		context = super(ConversationMessageFormView, self).get_context_data(**kwargs)
		context['object'] = self.get_object()
		return context

class RecentMessgaesListView(LoginRequiredMixin, AjaxResponseMixin, ListView):
	template_name = 'conversations/recent_messages.html'
	paginate_by = 10

	def get_queryset(self):
		return Message.objects.order_by('-date')

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

class ConversationExportView(LoginRequiredMixin, View):

	def get(self, request, *args, **kwargs):
		conversations = Conversation.objects.all()
		response = HttpResponse(mimetype='text/csv')
		response['Content-Disposition'] = 'attchment; filename=conversations-%s.csv' % date.today()

		writer = csv.writer(response)

		for conversation in conversations:
			try:
				writer.writerow(['User', 'Title', 'Created', 'Tags', 'Slug'])
				writer.writerow([conversation.user, conversation.title, conversation.created, conversation.tag_titles(), conversation.slug])
				writer.writerow(['Messages:', '', '', '', ''])
				writer.writerow(['User', 'date', 'text', '', ''])
			except:
				pass
			for message in conversation.messages.all():
				try:
					writer.writerow([message.user, message.date, message.text, '', ''])
				except:
					pass
			writer.writerow(['', '', '', '', ''])
		return response
