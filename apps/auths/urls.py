from django.urls import path

# Local
from .views import character_info , create_character ,get_races , view_armors , equip_armor
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
    path('armors/<int:character_id>/<str:armor_type>/', view_armors, name='view_armors'),

    path('equip_armor/<int:character_id>/<int:armor_id>/<str:armor_type>/', equip_armor, name='equip_armor'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)