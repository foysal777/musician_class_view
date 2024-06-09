from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView
from musician_app.models import musicModel
from album_app.models import albumModel
from musician_app.forms import modelForm
from album_app.forms import albumForm

class HomeView(TemplateView):
    template_name = 'home.html'

class DatabaseView(ListView):
    template_name = 'database.html'
    context_object_name = 'data'

    def get_queryset(self):
        combined_data = musicModel.objects.select_related('musicians').all()
        data_list = [{
            'id': item.musician_id,
            'musician_name': f"{item.first_name} {item.last_name}",
            'email': item.email,
            'instrument': item.instrument,
            'album_name': item.musicians.Album_name,
            'album_rating': item.musicians.Album_Rating,
            'release_date': item.musicians.Album_release_Date,
        } for item in combined_data]
        return data_list

class EditAlbumView(UpdateView):
    model = albumModel
    form_class = albumForm
    template_name = 'album.html'
    success_url = reverse_lazy('database')

class EditNameView(UpdateView):
    model = musicModel
    form_class = modelForm
    template_name = 'musician.html'
    success_url = reverse_lazy('database')

class DeletePostView(DeleteView):
    model = musicModel
    success_url = reverse_lazy('database')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
