from django import forms
from .models import Blogger,BlogPost


class BloggerForm(forms.ModelForm):
    class Meta:
        model = Blogger
        fields = ['text']
        labels = {'text': ''}
        

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}