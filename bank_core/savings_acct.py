from bank_core.interest_rewards_acct import InterestRewardsAcct

class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initial_amount, acct_name):
        super().__init__(initial_amount, acct_name)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount + self.fee)
            self.get_balance()
        except BalanceException as error:
            raise error