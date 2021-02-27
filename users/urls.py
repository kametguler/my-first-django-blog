from django.urls import path
from .views import register, profile , edit_profile
from django.contrib.auth import views as auth_views


urlpatterns=[
    path('kayit-ol/', register, name='register'),
    path('giris-yap', auth_views.LoginView.as_view(), name='login'),
    path('cikis-yap/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('profil/', profile, name='profile'),
    path('profil/duzenle/', edit_profile, name='edit_profile'),

    path('sifre-sifirlama/', auth_views.PasswordResetView.as_view(template_name='users-password-reset/password_reset.html'), name='password_reset'),
    path('sifre-sifirlama/tamamlandi/', auth_views.PasswordResetDoneView.as_view(template_name='users-password-reset/password_reset_done.html'), name='password_reset_done'),
    path('sifre-sifirlama-onaylandi/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='users-password-reset/password_reset_confirm.html'), name='password_reset_confirm'),
    path('sifre-sifirlama-basarili/', auth_views.PasswordResetCompleteView.as_view(template_name='users-password-reset/password_reset_complete.html'), name='password_reset_complete'),
]