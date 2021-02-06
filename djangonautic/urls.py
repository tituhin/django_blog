
import accounts
from os import name
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from . import views, settings
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin', admin.site.urls),
    path('articles/', include('articles.url')),
    path('accounts/', include('accounts.urls')),
    path('about/', views.about,name = 'about'),
    path('',views.home,name='home'),
    

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

