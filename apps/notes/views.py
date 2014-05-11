from django.http import HttpResponseRedirect
from django.views.generic import FormView, DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from braces.views import LoginRequiredMixin, AjaxResponseMixin

from models import Note
from forms import NoteForm

# Create your views here.

class NoteListView(LoginRequiredMixin, AjaxResponseMixin, ListView):
	model = Note

class NoteFormView(LoginRequiredMixin, AjaxResponseMixin, FormView):
	form_class = NoteForm
	template_name = 'notes/form.html'

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.user = self.request.user
		self.object.save()
		return HttpResponseRedirect(self.object.get_absolute_url())

	def form_invalid(self, form):
		return super(NoteFormView, self).form_invalid(form)

class NoteDetailView(LoginRequiredMixin, AjaxResponseMixin, DetailView):
	model = Note