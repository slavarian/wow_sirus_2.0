from .views import main , custom_logout
from django.urls import path 

urlpatterns = [
    path('', main, name='main_page'),
    path('logout/', custom_logout, name='logout'),
]
