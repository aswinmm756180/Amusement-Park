from django.forms import ModelForm
from django import forms
from .models import Foodlist

class FoodDetailsForm(forms.ModelForm):
    class Meta:
        model= Foodlist
        fields='__all__' 