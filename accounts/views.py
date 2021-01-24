from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, TemplateView, UpdateView
from .forms import CustomUserCreationForm

# Create your views here.

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

# class ProfileView(LoginRequiredMixin, TemplateView):
#     model = UserProfile
#     template_name = 'profile.html'
#     login_url = 'login'

# class ProfileUpdateView(LoginRequiredMixin, UpdateView):
#     model = UserProfile
#     template_name = 'profile_edit.html'
#     fields = ['bio', 'standard', 'division', 'school']
#     login_url = 'login'
