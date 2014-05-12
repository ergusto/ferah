from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render
from django.utils import simplejson as json
from django.views.generic import View, TemplateView, FormView, DetailView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse_lazy

from braces.views import LoginRequiredMixin, AjaxResponseMixin, JSONResponseMixin

from apps.utils.http import JSONResponse

from apps.conversations.models import Conversation

from models import Tag
from forms import SimpleTagForm, TagForm
from utils.serializers import TagSerializer

class TagListView(LoginRequiredMixin, ListView):
	model = Tag

	def get_queryset(self):
		return Tag.objects.all().order_by('slug')

class TagDetailView(LoginRequiredMixin, DetailView):
	model = Tag

	def get_object(self, **kwargs):
		return Tag.objects.get(slug=self.kwargs['slug'])

class TagDeleteView(LoginRequiredMixin, DeleteView):
	model = Tag
	success_url = reverse_lazy('tags_list')

	def get_object(self, **kwargs):
		return Tag.objects.get(slug=self.kwargs['slug'])

class AddTagToConversationFormView(LoginRequiredMixin, FormView):
	form_class = TagForm
	template_name = 'tags/conversation_tag_form.html'

	def get_object(self, **kwargs):
		return Conversation.objects.get(slug=self.kwargs['slug'])

	def get_success_url(self):
		object = self.get_object()
		return object.get_absolute_url()

	def get_context_data(self, **kwargs):
		context = super(AddTagToConversationFormView, self).get_context_data(**kwargs)
		context['object'] = self.get_object()
		return context

	def form_valid(self, form):
		conversation = self.get_object()
		tag = conversation.add_tag(form.cleaned_data['title'])
		if self.request.is_ajax():
			serializer = TagSerializer(tag)
			return JSONResponse({'tag': serializer.data, 'object_remove_tag_url': conversation.get_remove_tag_url()}, status=200)
		return HttpResponseRedirect(self.get_success_url())

	def form_invalid(self, form):
		if self.request.is_ajax():
			return JSONResponse(form.errors, status=400)
		return super(AddTagToConversationFormView, self).form_invalid(form)

class RemoveTagFromConversationView(LoginRequiredMixin, FormView):
	form_class = TagForm
	template_name = 'tags/conversation_remove_tag_form.html'

	def get_object(self, **kwargs):
		return Conversation.objects.get(slug=self.kwargs['slug'])

	def get_success_url(self):
		self.object = self.get_object()
		return self.object.get_absolute_url()

	def get_context_data(self, **kwargs):
		context = super(RemoveTagFromConversationView, self).get_context_data(**kwargs)
		context['object'] = self.get_object()
		return context

	def form_valid(self, form):
		conversation = self.get_object()
		tags = conversation.remove_tag(form.cleaned_data['title'])
		if self.request.is_ajax():
			serializer = TagSerializer(tags)
			return JSONResponse({'tags': serializer.data, 'object_remove_tag_url': conversation.get_remove_tag_url()}, status=200)
		return HttpResponseRedirect(self.get_success_url())

	def form_invalid(self, form):
		if self.request.is_ajax():
			return JSONResponse(form.errors, status=400)
		return super(RemoveTagFromConversationView, self).form_invalid(form)