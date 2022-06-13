from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views
from django.contrib.auth.decorators import login_required

# Django nos provee de clases ya hechas para el login, logout y password_reset
urlpatterns = [
    # Vista de inicio
    path('', inicio),
    # Esta url no se mostrara si el usuario esta logeado
    path('registro/', registro),
    # Clase que usa django para el login, esta url no se mostrara si el usuario esta logeado
    path('login/', LoginView.as_view(template_name='vistas/login.html')),
    # Clase que usa django para el logout
    path('logout/', login_required(LogoutView.as_view(template_name='vistas/logout.html'))),
    # Clase que usa django para el password_reset
    path('cambiar-password/', views.PasswordChangeView.as_view(template_name='vistas/cambiar-password.html', success_url = '/')),
    
    # Clases que usa django para el forgot_password
    path('reset-password/', views.PasswordResetView.as_view(template_name='vistas/recuperar-password/password-reset.html'), name='password_reset'),
    path('reset-password-send/', views.PasswordResetDoneView.as_view(template_name='vistas/recuperar-password/email-send.html'), name='password_reset_done'),
    path('change-password/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(template_name='vistas/recuperar-password/change-password.html'), name='password_reset_confirm'),
    path('reset-password-complete/', views.PasswordResetCompleteView.as_view(template_name='vistas/recuperar-password/reset-password-complete.html'), name='password_reset_complete'),
]