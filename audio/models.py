from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)

class AudioFile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=255)
    file_path = models.CharField(max_length=255)
    upload_date = models.DateTimeField(auto_now_add=True)
    file_format = models.CharField(max_length=10)

class Metadata(models.Model):
    audio_file = models.ForeignKey('AudioFile', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True, blank=True)
    artist = models.CharField(max_length=255, null=True, blank=True)
    album = models.CharField(max_length=255, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    genre = models.CharField(max_length=50, null=True, blank=True)
    track_number = models.IntegerField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)  # Duration in seconds
    bitrate = models.IntegerField(null=True, blank=True)
    sample_rate = models.IntegerField(null=True, blank=True)