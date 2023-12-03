from .views import main
from django.urls import path 
from .views import custom_logout

urlpatterns = [
    path('', main, name='main_page'),
    path('logout/', custom_logout, name='logout'),
]
