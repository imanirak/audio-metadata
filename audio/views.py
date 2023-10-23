from django.shortcuts import render
from django.urls import reverse
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
    success_url = 'audio/success/'# Redirect to a success page after upload

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'File uploaded successfully.')
        print("Form valid method executed")
        print(self)
        return super().form_valid(form)
    
def success_message(request):
    return render(request, 'audio/success_message.html')

        
def index(request):
    audio_upload_form = AudioFileUploadForm()
    return render(request, 'audio/index.html', {'audio_upload_form': audio_upload_form})