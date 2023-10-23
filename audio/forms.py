from django import forms
from audio.models import AudioFile

class AudioFileUploadForm(forms.ModelForm):
    class Meta:
        model = AudioFile
        fields = ['file_field']  # Replace 'file_field' with the name of your file field

    file_field = forms.FileField(widget=forms.FileInput(attrs={'accept': 'audio/*'}))