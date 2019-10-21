from . import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from accounts import views


urlpatterns = [
    path('', include('doit.urls')),
    path('join/', views.JoinView.as_view(), name = 'join'),
    path('login/', auth_views.LoginView.as_view(template_name = 'accounts/login.html'), name = 'login'),
    path('profile/', views.ProfileView.as_view(), name = 'profile'),
    path('profile/update/', views.ProfileUpdateView.as_view(), name = 'update_profile'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'accounts/logout.html'), name = 'logout'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 