from django.urls import path

from .views import SignUpView
urlpatterns = [
    path('signup/',SignUpView.as_view(), name='signup'),
    path('logout/',SignUpView.as_view(), name='logout'),
    path('login/',SignUpView.as_view(), name='login'),
    # path('<str:username>/', ProfileView.as_view(), name='profile'),
    # path('accounts/edit/', ProfileUpdateView.as_view(), name='profile_edit')
]
