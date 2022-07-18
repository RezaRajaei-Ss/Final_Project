from django import forms
from .models import *
from ckeditor.fields import RichTextField


class PostForm(forms.ModelForm):
    description = RichTextField()

    class Meta:
        model  = Post
        fields = ('description',)
