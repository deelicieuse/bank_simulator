class BalanceException(Exception):
    pass


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

class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete.")
        self.get_balance()

class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initial_amount, acct_name):
        super().__init__(initial_amount, acct_name)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount + self.fee)
            print("\nWithdraw Complete.")
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")