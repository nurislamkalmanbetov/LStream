from django.urls import path 
from .views import GameListView, GamesDetail



urlpatterns = [
    path('game_list/', GameListView.as_view(), name='game_list'), 
]























    # path('game_detail/<int:pk>/', GamesDetail.as_view(), name='game_detail'),
