from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import modelForm
from .models import musicModel

class MusicianCreateView(CreateView):
    model = musicModel
    form_class = modelForm
    template_name = 'musician.html'
    success_url = reverse_lazy('musician')
 