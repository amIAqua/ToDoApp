from django.urls import path
from . import views

app_name = 'doit'

urlpatterns = [
    path('', views.WelcomePageView.as_view(), name = 'welcome_page'),
    path('plans/', views.MainUserScreenTable.as_view(), name = 'plans'),
    path('delete/<int:id>', views.delete_table_line, name = 'delete'),
    path('edit/<int:id>', views.edit_table_line, name = 'edit'),
    path('about/', views.about, name = 'about'),
]