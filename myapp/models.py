# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Login(models.Model):
	userName=models.EmailField("Enter a Valid Email Address")
