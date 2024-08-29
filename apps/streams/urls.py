from django.urls import path 
from .views import *
from apps.main.urls import IndexView
# from ..main.urls import IndexView 



urlpatterns = [
    
    path('profile_start_stream/', StartStreamView.as_view(), name='profile_start_stream'),
    path('live_stream/<int:stream_id>/', LiveStreamView.as_view(), name='live_stream'),
    path('end_stream/<int:stream_id>/', EndStreamView.as_view(), name='end_stream'),

    path('streams/', StreamListView.as_view(), name='streams'),
]

