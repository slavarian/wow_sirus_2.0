from django.urls import path
from .views import FileListView, FileDownloadView

urlpatterns = [
    path('download/', FileListView.as_view(), name='download'),
  
    path('download/<int:file_id>/', FileDownloadView.as_view(), name='file_download'),
    
]