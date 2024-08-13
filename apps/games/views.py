from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView


class GameListView(ListView):
    model = Games 
    template_name = 'pages/game_list.html'
    context_object_name = 'games'
    queryset = Games.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context
    
class GamesDetail(DetailView):
    model = Games
    template_name = 'pages/game_detail.html'
    context_object_name = 'game'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        # order_by('-download_count')[:5]  # Получить 5 самых скачиваемых игр
        return context