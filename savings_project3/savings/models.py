# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.


class Bank(models.Model):
    name = models.CharField(max_length = 50)
    abbreviation = models.CharField(max_length = 8)
    def __str__(self):
        return self.name

class Client(models.Model):
    firstname = models.CharField(max_length = 20)
    lastname = models.CharField(max_length = 20)

    def __str__(self):
        return (self.lastname + " " + self.firstname)

class Deposit(models.Model):
    name = models.CharField(max_length = 40)
    value = models.IntegerField()
    interest = models.DecimalField(max_digits = 4, decimal_places = 2)
    start_date = models.DateField()
    stop_date = models.DateField()
    comment = models.TextField(max_length = 100)
    closed = models.BooleanField(default = False)  # czy zamknięta
    bank = models.ForeignKey(Bank, on_delete = models.CASCADE)
    client = models.ForeignKey(Client, on_delete = models.CASCADE)

    def __str__(self):
        return (self.bank.name + " (" + str(self.start_date) + " - " + str(self.stop_date) + ")" )

    def isExpired(self):
        return self.stop_date >= timezone.now().date()