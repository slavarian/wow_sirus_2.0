from django import forms
from news.models import News

class NewsCreationForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content']