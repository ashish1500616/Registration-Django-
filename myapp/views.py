# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# from django.http import HttpResponse
from myapp.forms import LoginForm

# Create your views here.
#
def hello(request):
    text = "welcome to my app !"
    return render(request,"myapp/base.html",{'text':text})


def connect(request):
	return render(request,"myapp/login.html",{})
	

def login(request):
	username="not logged in"
	if(request.method) =="POST":
		myLoginDetails=LoginForm(request.POST)

		if myLoginDetails.is_valid():
			username=myLoginDetails.cleaned_data['username']
		else:
			myLoginDetails=LoginForm()
	return render(request,'myapp/loggedin.html',{'username':username})
