from django.shortcuts import render
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from audio.models import AudioFile
from .forms import AudioFileUploadForm
from django.utils.decorators import method_decorator
from django.contrib import messages
@method_decorator(login_required, name='dispatch')
class AudioFileUploadView(CreateView):
    model = AudioFile
    form_class = AudioFileUploadForm
    template_name = 'audio/audiofile_upload.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'File uploaded successfully.')
        print("Form valid method executed")
        return super().form_valid(form)
    
    def get_success_url(self):
        # Return the URL of the current view
        return reverse('index')

@method_decorator(login_required, name='dispatch')
class AudioFileListView(ListView):
    model = AudioFile
    form_class = AudioFileUploadForm
    template_name = 'audio/audiofile_list.html'
        
def index(request):
    audio_upload_form = AudioFileUploadForm()
    audio_files = AudioFile.objects.all()

    context = {
        'audio_files': audio_files,
        'audio_upload_form' : audio_upload_form
    }

    return render(request, 'audio/index.html', context)