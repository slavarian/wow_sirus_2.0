from django.urls import path
from .views import FileListView, FileUploadView, FileDownloadView

urlpatterns = [
    path('download/', FileListView.as_view(), name='download'),
    path('upload/', FileUploadView.as_view(), name='file_upload'),
    path('download/<int:file_id>/', FileDownloadView.as_view(), name='file_download'),
    
]