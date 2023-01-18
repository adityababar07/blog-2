from django import forms
# from django.contrib.auth.forms import CommentCreationForm
from .models import Comment

class CommentForm(forms.Form):
    class Meta:
        model = Comment
        fields = ('comment')
