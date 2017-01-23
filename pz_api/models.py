from __future__ import unicode_literals

import uuid

from django.db import models
from django.contrib.auth.models import User


class BankAccount(models.Model):
    """
    Info about a bank account.

    :param uuid id: UUID
    :param str name: name.
    :param str description: description.
    :param decimal balance: balance.
    :param str currency: currency.
    :param date created_at: date of creation.
    :param date updated_at: date of the last update.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    """
    UUID.

    An instance of :class:`django.models.UUIDField`
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    """
    User owner.

    An instance of :class:`django.contrib.auth.models.User`
    """

    name = models.CharField(max_length=255)
    """
    Name.

    An instance of :class:`django.db.models.CharField`
    """

    description = models.CharField(max_length=255)
    """
    Description.

    An instance of :class:`django.db.models.CharField`
    """

    balance = models.DecimalField(max_digits=999999999, decimal_places=2)
    """
    Balance.

    An instance of :class:`django.db.models.DecimalField`
    """

    currency = models.CharField(max_length=3)
    """
    Currency.

    An instance of :class:`django.db.models.CharField`
    """

    created_at = models.DateTimeField(auto_now_add=True)
    """
    Date of creation.

    An instance of :class:`django.db.models.DateTimeField`
    """

    updated_at = models.DateTimeField(auto_now=True)
    """
    Date of the last update.

    An instance of :class:`django.db.models.DateTimeField`
    """

    def __str__(self):
        return self.name


class Category(models.Model):
    """
    Info about a category.

    :param uuid id: UUID.
    :param int user_id: id of user.
    :param int parent_id: id of parent category.
    :param str name: name.
    :param URLField icon: icon path.
    :param binary type: type of category (input/output).
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    """
    UUID.

    An instance of :class:`django.models.UUIDField`
    """

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    """
    ID of user.

    An instance of :class:`pz_api.models.BankAccount`
    """

    parent_id = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    """
    ID of category.

    An instance of :class:`pz_api.models.Category`
    """

    name = models.CharField(max_length=255)
    """
    Name.

    An instance of :class:`django.db.models.CharField`
    """

    icon = models.URLField()
    """
    Icon path.

    An instance of :class:`django.db.models.URLField`
    """

    type = models.BinaryField()
    """
    Amount.

    An instance of :class:`django.db.models.DecimalField`
    """

    def __str__(self):
        return self.name


class Transaction(models.Model):
    """
    Info about a transaction.

    :param uuid id: UUID.
    :param BankAccount bank_account_id: id of bank account.
    :param Category category_id: id of category.
    :param decimal amount: amount.
    :param date created_at: date of creation.
    :param date updated_at: date of the last update.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    """
    UUID.

    An instance of :class:`django.models.UUIDField`
    """

    bank_account_id = models.ForeignKey(BankAccount, on_delete=models.CASCADE)
    """
    ID of bank account.

    An instance of :class:`pz_api.models.BankAccount`
    """

    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    """
    ID of category.

    An instance of :class:`pz_api.models.Category`
    """

    description = models.CharField(max_length=255)
    """
    Description.

    An instance of :class:`django.db.models.CharField`
    """

    date = models.DateTimeField()
    """
    Date of transaction.

    An instance of :class:`django.db.models.DateTimeField`
    """

    amount = models.DecimalField(max_digits=999999999, decimal_places=2)
    """
    Amount.

    An instance of :class:`django.db.models.DecimalField`
    """

    created_at = models.DateTimeField(auto_now_add=True)
    """
    Date of creation.

    An instance of :class:`django.db.models.DateTimeField`
    """

    updated_at = models.DateTimeField(auto_now=True)
    """
    Date of the last update.

    An instance of :class:`django.db.models.DateTimeField`
    """

    def __str__(self):
        return self.description
