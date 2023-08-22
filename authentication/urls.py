from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("u/signup", views.register, name="register"),
    path("u/login", views.login, name="login"),
    
    # urls routes for reset password 
    path("o/password-reset/verify", auth_views.PasswordResetView.as_view(
        template_name = 'authentication/password-reset.html'
        # html_email_template_name = 'emails/mail.html'
    ), name = "password_reset"),
    
    path('o/password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name = 'authentication/password_reset_done.html'
    ), name = "password_reset_done"),
    
    path('o/password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name = 'authentication/password_reset_confirm.html'
    ), name= "password_reset_confirm"),
    
    path('o/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name = 'authentication/password_reset_complete.html'
    ), name = "password_reset_complete"
    ),
]