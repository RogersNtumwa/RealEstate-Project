from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('pages.urls')),
    path('listings/', include('listing.urls')),
    path('admin/', admin.site.urls)

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
