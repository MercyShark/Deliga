from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.UserRegistrationView.as_view(),name='register'),
    path('login/',views.UserLoginView.as_view(),name='login'),
    path('user-info/',views.UserInfoView.as_view(),name='user-info'),
    path('change-password/',views.UserChangePasswordView.as_view(),name='change-password'),
    path('check-email/',views.UserCheckEmailAvailabilityView.as_view(),name='check-email'),
    path('check-username/',views.UserCheckUsernameAvailabilityView.as_view(),name='check-username'),
]
