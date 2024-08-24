from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView


class GameListView(ListView):
    model = Games 
    template_name = 'pages/game_list.html'
    context_object_name = 'games'
    queryset = Games.objects.all().order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['category'] = Category.objects.all()
        context['top_down'] = Games.objects.order_by('-download_count')[:6]
        return context
    
class GamesDetail(DetailView):
    model = Games
    template_name = 'pages/game_detail.html'
    context_object_name = 'game'
    queryset = Games.objects.all()