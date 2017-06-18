from django import forms
from .models import  User_detail


class LoginForm(forms.Form):
    user = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())

class PostForm(forms.ModelForm):
	# name=forms.CharField(max_length=20)
	# emailAdd=forms.EmailField(max_length=264)
	# text=forms.CharField(widget=forms.Textarea)

	class Meta:
		model=User_detail
		fields="__all__"  