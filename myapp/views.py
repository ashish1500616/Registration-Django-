# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# from django.http import HttpResponse
from myapp.forms import LoginForm, PostForm, UserForm, UserProfileForm
from myapp.models import User_detail
from django import forms
# Create your views here.
#


def hello(request):
    text = "welcome to my app !"
    return render(request, "myapp/base.html", {'text': text})


def connect(request):
    return render(request, "myapp/loginpage.html",)


def login(request):
    username = "not logged in"
    if request.method == "POST":
        myLoginDetails = LoginForm(request.POST)

        if myLoginDetails.is_valid():
            username = myLoginDetails.cleaned_data['username']
        else:
            myLoginDetails = LoginForm()
    return render(request, 'myapp/loggedin.html', {'username': username})


def show_user(request):
    user_dic = User_detail.objects.order_by('firstname')
    return render(request, 'myapp/users.html', {'user_list': user_dic})

# order_by('firstname')


def show_basic_form(request):
    form = PostForm()
    return render(request, 'myapp/form_page.html', {'form': form})


def show_form(request):
    form = PostForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=True)
            print("Form Validattion Successful")
            print("Nmae:" + form.cleaned_data['firstname'])
            print("Email:" + form.cleaned_data['email'])
            return show_user(request)
        else:
            print("Error Form Invalid")
    return render(request, 'myapp/forms.html', {'form': form})


# form form for registeration
def toRegister(request):
    registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)

            # sets one to one relation
            profile.user = user

            if 'profile_pic' in request.FILES:
                # same syntax for uplaoding any kind of file
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'myapp/registeration.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered,
    })
