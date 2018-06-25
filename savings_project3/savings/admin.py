# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Bank, Client, Deposit
# Register your models here.

admin.site.register(Bank)
admin.site.register(Client)
admin.site.register(Deposit)