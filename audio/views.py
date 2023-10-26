from django.shortcuts import render
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from audio.models import AudioFile
from .forms import AudioFileUploadForm
from django.utils.decorators import method_decorator
from django.contrib import messages
from mutagen import File
from mutagen.mp3 import MP3
from mutagen.flac import FLAC



def view_audio_metadata(request, audio_file_id):
    audio_file = AudioFile.objects.get(id=audio_file_id)
    audio_file_path = audio_file.audio.path

    # Load the audio file using Mutagen
    audio = File(audio_file_path)
    for key in audio:
        print(f"{key}: {audio[key]}")
    # Access metadata tags
    title = audio.get('TIT2', ['Unknown Title'])[0]
    artist = audio.get('TPE1', ['Unknown Artist'])[0]
    comment = audio.get('COMM', [''])[0]
    genre = audio.get('TCON', ['Unknown Genre'])[0]
    duration = audio.info.length
    track_number = audio.get('TRCK', ['Unknown Track'])[0]
    album = audio.get('album')
    print(audio)

    return render(request, 'audio/audiofile_metadata.html', {
        'audio_file': audio_file,
        'title': title,
        'artist': artist,
        'album': album,
        'duration': duration,
        'genre': genre,
        'track_number': track_number,
    })

@method_decorator(login_required, name='dispatch')
class AudioFileUploadView(CreateView):
    model = AudioFile
    form_class = AudioFileUploadForm
    template_name = 'audio/audiofile_upload.html'
   
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        
    # Save the form instance without metadata
        instance = form.save()
        metadata = view_audio_metadata(self.request, instance.id)
        print(metadata)

        messages.success(self.request, 'File uploaded, and metadata extracted and saved successfully')
        return super().form_valid(form)


    def get_success_url(self):
        # Return the URL of the current view
        messages.success(self.request, '')
        return reverse('index')

@method_decorator(login_required, name='dispatch')
class AudioFileListView(ListView):
    model = AudioFile
    form_class = AudioFileUploadForm
    template_name = 'audio/audiofile_list.html'

    def get_queryset(self):
        # Use select_related to fetch the related Metadata instance
        return AudioFile.objects.select_related('metadata')


def index(request):
    audio_upload_form = AudioFileUploadForm()
    audio_files = AudioFile.objects.all()

    context = {
        'audio_files': audio_files,
        'audio_upload_form' : audio_upload_form
    }

    return render(request, 'audio/index.html', context)