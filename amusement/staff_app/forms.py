from django.forms import ModelForm
from django import forms
from .models import Foodlist






class FoodDetailsForm(forms.ModelForm):
    class Meta:
        model= Foodlist
        fields='__all__' 






from django import forms
from .models import staff

class StaffRegistrationForm(forms.ModelForm):
    class Meta:
        model = staff
        fields = ['name', 'usernanme', 'email', 'password', 'password2']
        widgets = {
            'password': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
        }



from django import forms
from django.contrib.auth.forms import AuthenticationForm

class StaffLoginForm(AuthenticationForm):
    class Meta:
        model = staff
        fields = ['username', 'password']



