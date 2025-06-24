import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

from bank_core.balance_exception import BalanceException
from bank_core.bank_accounts import BankAccount
from bank_core.interest_rewards_acct import InterestRewardsAcct
from bank_core.savings_acct import SavingsAcct

class BankGui:
    def __init__(self, root):
        self.root = root
        root.title("Bank ATM Simulation")
        root.geometry("550x580")
        root.resizeable(False,False)

        pass