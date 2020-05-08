from django import forms
from django.contrib.auth.models import User
from learning_app.models import UserProfileInfo


class UserForm(forms.ModelForm):
    #this is used to hide the password
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields=('__all__')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model =UserProfileInfo
        fields =('protfolio','profile_pic')
