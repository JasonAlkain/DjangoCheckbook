from django.db import models

# Create your models here.

class Account(models.Model):
    # First Name on the account
    first_name = models.CharField(max_length=50)
    # Last Name on the account
    last_name = models.CharField(max_length=50)
    # Starting Balance of the Class in hours
    starting_balance = models.DecimalField(max_digits=15, decimal_places=2)
    # Add the models manager
    Accounts = models.Manager()

    # Returns a more comprehensive name
    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

TransactionTypes = {
    ('deposit', 'deposit'),
    ('withdrawal', 'withdrawal'),
}

class Transaction(models.Model):
    # Date of Transaction
    date = models.DateField()
    # Type of Transaction [Deposit or Withdrawal]
    type = models.CharField(max_length=10, choices=TransactionTypes)
    # Amount
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    # Description
    description = models.CharField(max_length=100)
    # Account it applies to [this is a Foreign Key]
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    # Add the models manager
    Transactions = models.Manager()

    # Returns a more comprehensive name
    def __str__(self):
        return '{} | {} | {}'.format(self.account, self.type, self.date)
