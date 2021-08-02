from django import forms
from .models import SampleName


class SampleNameForm(forms.ModelForm):
    class Meta:
        model = SampleName
        fields = ['first_name', 'last_name']
