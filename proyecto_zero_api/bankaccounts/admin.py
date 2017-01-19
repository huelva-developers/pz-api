from django.contrib import admin
from proyecto_zero_api.bankaccounts.models import BankAccount

class BankAccountAdmin(admin.ModelAdmin):
    pass

admin.site.register(BankAccount, BankAccountAdmin)
