from django.shortcuts import render
from django.views.generic import TemplateView

from braces.views import LoginRequiredMixin, AjaxResponseMixin

# Create your views here.

class UtilsView(LoginRequiredMixin, TemplateView):
	template_name = 'utils/utils.html'