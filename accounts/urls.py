from os import name
from accounts.views import signup_view
from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/',views.login_view, name='login'),
    path('logout/',views.logout_view,name='logout'),
]
