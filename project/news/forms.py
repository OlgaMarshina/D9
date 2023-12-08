from django import forms
from django.core.exceptions import ValidationError

from .models import Post, Category


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['id','author', 'title', 'content', 'post_type', 'categories']