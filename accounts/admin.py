from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    models = CustomUser
    list_display = ['id', 'email', 'username', 'age', 'bio', 'standard', 'division', 'house', 'stream', 'school', 'is_staff']


admin.site.register(CustomUser, CustomUserAdmin)
