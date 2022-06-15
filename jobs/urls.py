from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


admin.site.site_header = "ADMINISTRATOR"
admin.site.site_title = "ONLINE RECRUITMENT PLATEFORM "
admin.site.index_title = "Welcome to our system"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jobsapp.urls')),
    path('', include('accounts.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
