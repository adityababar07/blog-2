from django.forms import ModelForm
# from django.contrib.auth.forms import CommentCreationForm
from .models import Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('comment', 'author')
