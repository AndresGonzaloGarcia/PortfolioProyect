
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name= 'home'),
    path('portfolio/', views.portfolio, name= 'portfolio'),
    path('about_me/', views.about_me, name= 'about_me'),
    path('contact/', views.contact ,name= 'contact'),
    
]
