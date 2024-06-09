from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import albumForm
from .models import albumModel

class AlbumCreateView(CreateView):
    model = albumModel
    form_class = albumForm
    template_name = 'album.html'
    success_url = reverse_lazy('album')
