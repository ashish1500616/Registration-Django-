from django import forms
from .models import User_detail, UserProfileInfo
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    user = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


class PostForm(forms.ModelForm):
    # name=forms.CharField(max_length=20)
    # emailAdd=forms.EmailField(max_length=264)
    # text=forms.CharField(widget=forms.Textarea)

    class Meta:
        model = User_detail
        fields = "__all__"

# model user form connected one to one.


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User  # connected to already defined mode in django.
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):

    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')
