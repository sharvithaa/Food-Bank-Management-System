from django import forms
from .models import User,FoodDonation,Order
from django.contrib.auth.forms import AuthenticationForm


class SignupForm(forms.ModelForm):
    USERTYPE_CHOICES = [
        ('volunteer', 'Volunteer'),
        ('ngo', 'NGO'),
        ('donor', 'Donor'),
    ]
    
    usertype = forms.ChoiceField(
        choices=USERTYPE_CHOICES,
        required=True,
        widget=forms.Select(attrs={'class': 'custom-select'}),
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'usertype']
        widgets = {'password': forms.PasswordInput()}
        
class Loginform(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'your-custom-class'})
        self.fields['password'].widget=forms.PasswordInput()

class FoodDonationForm(forms.ModelForm):
    class Meta:
        model = FoodDonation
        fields = '__all__'  

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'quantity', 'place'] 