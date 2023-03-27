from django import forms
from .models import FileMs



class modelform(forms.Form):
    class meta:
        model = FileMs
        fields = '__all__'


class NameForm(forms.Form):
    rute = forms.CharField(label='rute', max_length=100)
    
