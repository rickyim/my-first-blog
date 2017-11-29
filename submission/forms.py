from django.contrib.auth.models import User
from django import forms
from .models import Submit

class UserForm(forms.ModelForm):#register
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        
class SubmitForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Submit
        fields = ('title', 'text',)
