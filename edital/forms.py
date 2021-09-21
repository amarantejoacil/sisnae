from django import forms
from .models import Edital


class EditalModelForm(forms.ModelForm):
    class Meta:
        model = Edital
        fields = '__all__'
