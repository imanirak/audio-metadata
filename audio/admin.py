from django.contrib import admin
from .models import AudioFile, Metadata
# Register your models here.
admin.site.register(Metadata)
admin.site.register(AudioFile)