from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('profile/privacy_settings',
         views.privacy_settings, name='privacy_settings'),
    path('profile/edit_profile/',
         views.edit_profile, name='edit_profile'),
    path('signup/', views.UserSignUpView.as_view(), name='signup'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('profile/password_change/', views.password_change, name='password_change'),
]
