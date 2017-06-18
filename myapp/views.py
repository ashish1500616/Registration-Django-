  # -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# from django.http import HttpResponse
from myapp.forms import LoginForm, PostForm
from myapp.models import User_detail
from django import forms
# Create your views here.
#


def hello(request):
    text = "welcome to my app !"
    return render(request, "myapp/base.html", {'text': text})


def connect(request):
    return render(request, "myapp/login.html", {})


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
    return render(request,'myapp/users.html', {'user_list': user_dic})

# order_by('firstname')
def show_basic_form(request):
    form=PostForm()
    return render(request,'myapp/form_page.html',{'form':form})

def show_form(request):
    form=PostForm(request.POST)
    if request.method =='POST':
        if form.is_valid():
            form.save(commit=True)
            print("Form Validattion Successful")
            print("Nmae:"+form.cleaned_data['firstname'])
            print("Email:"+form.cleaned_data['email'])
            return show_user(request)
        else:
            print("Error Form Invalid")
    return render(request,'myapp/forms.html',{'form':form})

