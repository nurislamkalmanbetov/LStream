
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Stream
from apps.games.models import Games



class StartStreamView(LoginRequiredMixin, View):

    def get(self, request):
        games = Games.objects.all()  # Получаем все игры
        return render(request, 'pages/profile_start_stream.html', {'games': games})

    def post(self, request):
        game = get_object_or_404(Games, id=request.POST.get('game'))

        stream = Stream.objects.create(
            streamer=request.user,
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            game=game,
            live=True,
        )
        # return redirect('streams/live_stream', stream.id) # Hasan
        # return redirect('streams:index', stream.id) # Amazon 
        return redirect('live_stream', stream.id)



class LiveStreamView(LoginRequiredMixin,View):

    def get(self, request, stream_id):
        stream = Stream.objects.get(id=stream_id,streamer=request.user, live=True)
        return render(request, 'pages/live_stream.html', {'streams': stream})



class EndStreamView(LoginRequiredMixin, View):

    def get(self, request, stream_id):
        stream = get_object_or_404(Stream, id=stream_id, streamer=request.user, live=True)
        stream.live = False
        stream.save()
        return redirect('profile_start_stream')


class StreamListView(ListView):
    model = Stream
    template_name = 'pages/streams.html'
    context_object_name = 'streams'
    queryset = Stream.objects.all()

