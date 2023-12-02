from django.urls import path

# Local
from .views import character_raiting 
from django.conf import settings
from django.conf.urls.static import static
from .views import character_views

urlpatterns = [
    path('info/<int:character_id>/', character_views, name='character_views'),
    path('raiting/', character_raiting, name='raiting'),
   

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)