from django.urls import path
from . import views

urlpatterns = [
     path("", views.index, name="index"),
     path('upload/', views.AudioFileUploadView.as_view(), name='audiofile_upload'),
   
]
