from django.contrib.auth.views import LogoutView
from django.urls import path

from accounts.views import CustomLoginView, CustomPasswordChangeView, SignUpView, ProfileView

app_name = 'accounts'
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-change/', CustomPasswordChangeView.as_view(), name='password-change'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile')
]