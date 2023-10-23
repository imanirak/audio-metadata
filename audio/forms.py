from django import forms
from audio.models import AudioFile

class AudioFileUploadForm(forms.ModelForm):
    class Meta:
        model = AudioFile
        fields = '__all__'  # Replace 'file_field' with the name of your file field

