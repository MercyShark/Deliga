from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.UserRegistrationView.as_view(),name='register_api'),
    path('login/',views.UserLoginView.as_view(),name='login_api'),
    path('change-password/',views.UserChangePasswordView.as_view(),name='change-password'),
    
]
