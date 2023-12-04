from .views import db_main_page
from django.urls import path 


urlpatterns = [
    path('', db_main_page, name='db_main_page'),
  
]
