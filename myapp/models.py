# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

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

