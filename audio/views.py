from django.shortcuts import render
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from audio.models import AudioFile, Metadata
from .forms import AudioFileUploadForm
from django.utils.decorators import method_decorator
from django.contrib import messages
from mutagen import File
from mutagen.mp3 import MP3
from mutagen.flac import FLAC
from datetime import datetime

def get_audio_metadata(request, audio_file_id):
    audio_file = AudioFile.objects.get(id=audio_file_id)
    audio_file_path = audio_file.audio.path

    # Load the audio file using Mutagen
    audio = File(audio_file_path)

    # Access metadata tags
    title = audio.get('TIT2', ['Unknown Title'])[0]
    artist = audio.get('TPE1', ['Unknown Artist'])[0]
    comment = audio.get('COMM::eng', [''])[0]
    genre = audio.get('TCON', ['Unknown Genre'])[0]
    duration = audio.info.length
    track_number = audio.get('TRCK', ['Unknown Track'])[0]
    album = audio.get('album', '')
    year_tag = audio.get('TDRC', [''])[0]
    year = str(year_tag)


    metadata = {
        'title': title,
        'artist': artist,
        'album': album,
        'year': year,
        'genre': genre,
        'duration': duration,
        'track_number': track_number,
        'comment': comment,
    }

    return metadata

def view_audio_metadata(request, audio_file_id):
    audio_file = AudioFile.objects.get(id=audio_file_id)
    audio_file_path = audio_file.audio.path

    audio = File(audio_file_path)
    title = audio.get('TIT2', ['Unknown Title'])[0]
    artist = audio.get('TPE1', ['Unknown Artist'])[0]
    comment = audio.get('COMM::eng', [''])[0]
    genre = audio.get('TCON', ['Unknown Genre'])[0]
    duration = audio.info.length
    track_number = audio.get('TRCK', ['Unknown Track'])[0]
    album = audio.get('album', '')
    year_tag = audio.get('TDRC', [''])[0]
    year = str(year_tag)


    return render(request, 'audio/audiofile_metadata.html', {
        'audio_file': audio_file,
        'title': title,
        'artist': artist,
        'album': album,
        'duration': duration,
        'genre': genre,
        'track_number': track_number,
        'comment': comment,
        'year': year
    })

@method_decorator(login_required, name='dispatch')
class AudioFileUploadView(CreateView):
    model = AudioFile
    form_class = AudioFileUploadForm
    template_name = 'audio/audiofile_upload.html'
   
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        
    # Save the form instance without metadata
        instance = form.save(commit=False)
        instance.save()
        metadata = get_audio_metadata(self.request, instance.id)
        print(metadata['title'])

        metadata_instance = Metadata.objects.create(
            audio_file=instance,
            title=metadata['title'],
            artist=metadata['artist'],
            album=metadata['album'],
            year=metadata['year'],
            genre=metadata['genre'],
            duration=metadata['duration'],
            track_number=metadata['track_number'],
            comment=metadata['comment'],
            
        )
        metadata_instance.save()
        print(metadata_instance.__dict__)
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