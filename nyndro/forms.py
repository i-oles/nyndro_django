from django import forms
from django.forms import ModelForm
from .models import Practice, Session


class PracticeDetailForm(ModelForm):
    CUSTOM = 0
    SESSION_CHOICES = (
    (27, '27'),
    (54, '54'),
    (108, '108'),
    (216, '216'),
    (324, '324'),
    (CUSTOM, '+'),
    )

    session_value = forms.ChoiceField(choices = SESSION_CHOICES, widget=forms.RadioSelect(), label='')
    
    class Meta:
        model = Session
        fields = ['session_value',]
 