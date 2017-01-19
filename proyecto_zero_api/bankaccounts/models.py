from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class BankAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=999999999, decimal_places=2)
    currency = models.CharField(max_length=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
