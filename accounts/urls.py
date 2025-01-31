from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register_view, name='register_view'),
    path('dashboard/', views.dashboard_view, name='dashboard_view'),
    path('update/', views.profile_update_view, name='profile_update_view'),
    path('changePassword/', views.change_password_view, name='change_password_view'),
    path('changePhoto/', views.update_profile_photo, name='change_photo_view'),

   #  path('profile/', views.UserProfileView.as_view(), name='profile_view'),
   path('logout/', views.logout_view, name='logout_view'),

   
]
