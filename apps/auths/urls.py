from django.urls import path

# Local
from .views import character_info , create_character ,get_races , equip_gear
from . import views
from django.contrib.auth import views as auth_views 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('character/<int:character_id>/', character_info, name='character_info'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('login/', auth_views.LogoutView.as_view(), name='logout'),
    path('create_character/', create_character, name='create_character'),
    path('get_races/', get_races, name='get_races'),
    path('equip_gear/', equip_gear, name='equip_gear'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)