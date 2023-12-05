from django import forms
from auths.models import MyUser


class AvatarChangeForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['avatar']
