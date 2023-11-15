from django import forms

from game_characters.models import Character

class GameCharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['nick_name','gender','fraction','race','specialization',]