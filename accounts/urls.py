from django.urls import path
from django.contrib.auth.models import User

from .views import SignUpView, ProfileView, ProfileUpdateView


urlpatterns = [
    path('signup/',SignUpView.as_view(), name='signup'),
    path('logout/',SignUpView.as_view(), name='logout'),
    path('login/',SignUpView.as_view(), name='login'),
    path('profile/<uuid:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/edit/<uuid:pk>/', ProfileUpdateView.as_view(), name='profile_edit')
]
