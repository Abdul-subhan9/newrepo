from django.urls import path, include
from account_app.views import UserChangePasswordView, UserRegistrationView, UserLogin, UserProfileView
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('change/',UserChangePasswordView.as_view(), name='changepassword'),

]
