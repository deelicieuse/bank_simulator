class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, intialAmount, acctName):
        self.balance = intialAmount
        self.name = acctName
        print(f"\nAccount '{self.name}' created."
              f"\nBalance = {self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount: '{self.name}'"
              f"\nBalance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\nDeposit Complete")
        self.getBalance()

    def viableTransaction(self, amount)
        if self.balance >= amount:
            return
        else:
            raise BalanceException
        f"\nSorry, account '{self.name} only has "
         f"a balance of ${self.balance:.2f}"

    def withdraw(self):
        pass