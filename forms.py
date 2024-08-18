from django import forms
import re
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile

class Meta:
    model = User
    fields = ('username', 'password1', 'password2', 'name', 'birth_date', 'phone_number', 'email',  'store_name', 'address')

    
    
class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    
class EditProfileForm(forms.ModelForm):
    email = forms.EmailField(required=True)  # User 모델의 email 필드를 폼에 추가

    class Meta:
        model = Profile
        fields = ['store_name', 'address', 'phone_number', 'birth_date']  # Profile 모델 필드들만 포함

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.fields['email'].initial = self.instance.user.email

    def save(self, commit=True):
        profile = super().save(commit=False)
        profile.user.email = self.cleaned_data['email']
        if commit:
            profile.user.save()
            profile.save()
        return profile

