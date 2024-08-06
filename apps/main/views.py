from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class IndexView(TemplateView):
    template_name = 'pages/index.html'



class BrowseView(TemplateView):
    template_name = 'pages/browse.html'

