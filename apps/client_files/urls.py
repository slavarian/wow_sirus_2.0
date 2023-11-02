from django.urls import path
from .views import upload_file

urlpatterns = [
    path('client/', upload_file, name='client'),
  
]