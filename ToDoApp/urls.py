from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from accounts import views

urlpatterns = [
    path('', include('doit.urls')),
    path('join/', views.join, name = 'join'),
    path('login/', auth_views.LoginView.as_view(template_name = 'accounts/login.html'), name = 'login'),
    path('profile/', views.profile, name = 'profile'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'accounts/logout.html'), name = 'logout'),
    path('admin/', admin.site.urls),
]