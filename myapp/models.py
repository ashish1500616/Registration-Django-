# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User
# Create your models here.


class Login(models.Model):
    username = models.CharField(max_length=20)

    def __unicode__(self):
        return self.username


class User_detail(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField(max_length=264, unique=True)

    def __unicode__(self):
        return self.firstname

# codes for user registration.
class UserProfileInfo(models.Model):
	#one to one relation between defined user model
 	user = models.OneToOneField(User)
 	# field to accept the portfolio site.
 	portfolio_site=models.URLField(blank=True)

 	profile_pic=models.ImageField(upload_to='profile_pic',blank=True)

 	def __unicode__(self):
 		return self.user.name

