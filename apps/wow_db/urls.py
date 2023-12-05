from .views import db_main_page , db_jewelry_page , db_weapon_page
from django.urls import path 


urlpatterns = [
    path('armor/', db_main_page, name='db_main_page'),
    path('jewelry/', db_jewelry_page, name='db_jewelry_page'),
    path('weapon/', db_weapon_page, name='db_weapon_page')
  
]
