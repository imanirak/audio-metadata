from django.urls import path
from . import views
from .views import success_message

urlpatterns = [
     #path("", views.index, name="index"),
     path('', views.AudioFileUploadView.as_view(), name='audiofile_upload'),
     path('upload/success/', views.success_message, name='upload_success'),
    
   
]
