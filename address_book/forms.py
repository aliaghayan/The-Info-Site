from django import forms
from .models import Address

class InfoForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['name','email','phone','company','address','city','state','zipcode']
