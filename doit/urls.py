from django.urls import path
from . import views

app_name = 'doit'

urlpatterns = [
    path('', views.welcome_page, name = 'welcome_page'),
    path('about/', views.about, name = 'about'),
]