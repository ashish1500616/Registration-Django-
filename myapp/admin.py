# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from myapp.models import Login, User_detail,UserProfileInfo

admin.site.register(Login)
admin.site.register(User_detail)
admin.site.register(UserProfileInfo)
