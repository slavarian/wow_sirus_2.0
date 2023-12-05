from .views import news_page
from django.urls import path 


urlpatterns = [
    path('', news_page, name='news_page'),
]
