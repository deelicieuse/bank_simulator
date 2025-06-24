class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, intialAmount, acctName):
        self.balance = intialAmount
        self.name = acctName
        print(f"\nAccount '{self.name}' created."
              f"\nBalance = {self.balance:.2f}")

    def get_balance(self):
        print(f"\nAccount: '{self.name}'"
              f"\nBalance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\nDeposit Complete")
        self.get_balance()

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
            print(f"\nWithdraw complete")
        except BalanceException as error:
            print(f"\n Withdraw interrupted: {error}")

    def transfer(self, amount, account):
        try:
            print("\n*********\n\nBeginning"
                  "Transfer...🚀")
            self.viable_transaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTranfer complete! "
                  "✅\n\n*********")
        except BalanceException as error:
            print(f"\nTranfer interrupted. ❌")

class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete.")
        self.get_balance()

class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee = 5