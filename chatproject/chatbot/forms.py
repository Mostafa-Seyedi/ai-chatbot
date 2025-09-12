from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ChatForm(forms.Form):
    user_input = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Type your message here...',
            'maxlength': '1000',  # Limit message length
            'required': True
        })
    )

class CustomUserCreationForm(UserCreationForm):
    """Custom registration form with Bootstrap styling"""
    
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Add Bootstrap classes and better placeholders to form fields
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Choose a username',
            'autocomplete': 'username'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your password',
            'autocomplete': 'new-password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm your password',
            'autocomplete': 'new-password'
        })
        
        # Update help texts
        self.fields['username'].help_text = '150 characters or fewer. Letters, digits and @/./+/-/_ only.'
        self.fields['password1'].help_text = 'Your password must contain at least 8 characters.'
        self.fields['password2'].help_text = 'Enter the same password as before, for verification.'