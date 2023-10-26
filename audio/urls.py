from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.AudioFileUploadView.as_view(), name='audiofile_upload'),
    path('list/', views.AudioFileListView.as_view(), name='audiofile_list'),
    path('audiofile_metadata/<int:audio_file_id>/', views.view_audio_metadata, name='audiofile_metadata'),
]
