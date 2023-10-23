from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from audio.models import AudioFile
from .forms import AudioFileUploadForm
from django.utils.decorators import method_decorator

#@method_decorator(login_required, name='dispatch')
class AudioFileUploadView(CreateView):
    model = AudioFile
    form_class = AudioFileUploadForm
    template_name = 'audio/audiofile_upload.html'
    success_url = '/upload/success/'  # Redirect to a success page after upload

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
def index(request):
    return HttpResponse("Main Dashboard.")