from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_set_audio',
        verbose_name='User Groups',
        blank=True,
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_set_audio',
        verbose_name='User Permissions',
        blank=True,
    )
    
class AudioFile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=255)
    audio = models.FileField(upload_to='audio/') 
    upload_date = models.DateTimeField(auto_now_add=True)
    file_format = models.CharField(max_length=10)

    def __str__(self):
        return self.file_name

class Metadata(models.Model):
    audio_file = models.OneToOneField(AudioFile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True, blank=True)
    artist = models.CharField(max_length=255, null=True, blank=True)
    album = models.CharField(max_length=255, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    genre = models.CharField(max_length=50, null=True, blank=True)
    track_number = models.IntegerField(null=True, blank=True)
    duration = models.FloatField(null=True, blank=True)
    authors = models.CharField(max_length=255, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
        
    def __str__(self):
        return f"{self.audio_file.file_name}Metadata"

