from django import forms
from .models import Board # models


class BaseBulletinBoard(forms.ModelForm):
    class Meta:
        model = Board
        fields= '__all__'
