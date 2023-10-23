from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.AudioFileUploadView.as_view(), name='audiofile_upload'),
    path("", views.index, name="index"),
]
