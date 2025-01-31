from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls import include
from .  import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('user/', include('accounts.urls')),
    path('Hospital/', include('Hospital.urls')),
    path('Ambulance/', include('Ambulance.urls')),
    path('Doctors/', include('Doctors.urls')),
    path('appointments/', include('appointments.urls')),
    path('store/', include('medicine_store.urls')),
    path('cart/', include('cart.urls')),
    path('', include('payments.urls')),


    # Reset password
   path(
       'password_reset/',
       auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),
       name='password_reset'
   ),
   path(
       'password_reset/done/',
       auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
       name='password_reset_done'
   ),
   path(
       'reset/<uidb64>/<token>/',
       auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
       name='password_reset_confirm'
   ),
   path(
       'reset/done/',
       auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
       name='password_reset_complete'
   ),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)