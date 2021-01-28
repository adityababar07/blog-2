from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, TemplateView, UpdateView
from django.shortcuts import get_object_or_404
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from django.contrib.auth.models import User 

# Create your views here.

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class ProfileView(LoginRequiredMixin, TemplateView):
    model = CustomUser
    template_name = 'profile.html'
    login_url = 'login'


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name = 'profile_edit.html'
    fields = ['username', 'email', 'age', 'bio', 'standard', 'division', 'house', 'stream', 'school']
    login_url = 'login'

