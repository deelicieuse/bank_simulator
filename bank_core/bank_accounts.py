from bank_core.balance_exception import BalanceException

class BankAccount:
    def __init__(self, intial_amount, acct_name):
        self.balance = intial_amount
        self.name = acct_name

    def get_balance(self):
        return


    def deposit(self, amount):
        self.balance = self.balance + amount


    def viable_transaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry, account '{self.name} only has "
             f"a balance of ${self.balance:.2f}")

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount)
            self.balance = self.balance - amount
        except BalanceException as error:
            raise error

    def transfer(self, amount, account):
        try:
            self.viable_transaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
        except BalanceException as error:
            raise error


