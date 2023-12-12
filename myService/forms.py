from django import forms
from .models import *


class ContactUs(forms.ModelForm):
    class Meta:
        model = Contact_Us_Form
        fields = "__all__"
