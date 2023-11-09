from django.urls import path

# Local
from .views import character_info
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('character/<int:character_id>/', character_info, name='character_info'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('login/', auth_views.LogoutView.as_view(), name='logout'),
]