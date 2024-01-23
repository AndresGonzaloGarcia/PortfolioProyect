
from django.contrib import admin
from django.urls import path
from core import views as core_views
from portfolio_section import views as portfolio_section_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.home, name= 'home'),
    path('portfolio/', portfolio_section_views.portfolio, name= 'portfolio'),
    path('about_me/', core_views.about_me, name= 'about_me'),
    path('contact/', core_views.contact ,name= 'contact'),
]

from django.conf import settings

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
    
