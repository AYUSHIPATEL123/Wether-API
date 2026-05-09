from django import forms
from .models import CustomUser
from django.contrib import messages

class UserForm(forms.ModelForm):
    confirm_password = forms.CharField(required=True,widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('first_name','last_name','username','phone','email','password','confirm_password')

    def clean(self):
            cleaned_data = super().clean()
            password = cleaned_data.get('password')
            confirm_password = cleaned_data.get('confirm_password')

            if password and confirm_password and password != confirm_password:
                
                raise forms.ValidationError("Password and confirm password do not match")
            
            if len(password) < 8:
                
                raise forms.ValidationError("Password must be at least 8 characters long")
            
            if CustomUser.objects.filter(email=cleaned_data.get('email')).exists():
                
                raise forms.ValidationError("Email already exists")
            
            return cleaned_data
        
    def save(self,commit=True):
            user = super().save(commit=False)
            user.set_password(self.cleaned_data['password'])
            if commit:
                user.save()
            return user


class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

