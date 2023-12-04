
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('client/', include('client_files.urls')),
    path('wow/',include('auths.urls')),
    path('character/',include('game_characters.urls')),
    path('',include('main.urls')),
    path('database/',include('wow_db.urls'))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)