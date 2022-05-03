from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('register',views.register, name="register"),
    path('login',views.login, name="login"),
    path('logout',views.logout, name="logout"),
    path('profile',views.profile, name="profile"),
    path('edit/<int:id>', views.edit_profile, name="edit_profile"),
    path('update/<int:id>', views.update_profile, name ="update_profile"), 
    
    #PASSWORD RESET
    path ('reset_password/', 
    auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),name= "password_reset"),
    path ('reset_sent/', 
    auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_sent.html"),name= "password_reset_done"),
    path ('password_confirm/<uidb64>/<token>/', 
    auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_confirm.html"),name= "password_reset_confirm"),
    path ('password_complete/', 
    auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_complete.html"),name= "password_reset_complete"),
]