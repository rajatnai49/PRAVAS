from django.urls import path

from . import views

app_name = "administration"

urlpatterns = [
    path('', views.home_view, name='home'),
    path('register', views.register_request, name='register'),
    path('login', views.login_request, name='login'),
    path('logout', views.logout_request, name='logout'),
    path('profile', views.profile_request, name='profile'),
]
