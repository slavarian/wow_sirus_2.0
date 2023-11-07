from django.urls import path
from .views import upload_file

urlpatterns = [
    path('file_add/', upload_file, name='client'),
  
]