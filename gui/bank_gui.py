import customtkinter as ctk
from tkinter import messagebox, simpledialog

from bank_core.balance_exception import BalanceException
from bank_core.bank_accounts import BankAccount
from bank_core.interest_rewards_acct import InterestRewardsAcct
from bank_core.savings_acct import SavingsAcct


class BankGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM SIMULATOR")
        self.root.geometry("600x700")
        self.root.resizable(False, False)

        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.accounts = {
            "CHECKING": BankAccount(1500.00, "CHECKING"),
            "SAVINGS": SavingsAcct(2500.00, "SAVINGS"),
            "REWARDS": InterestRewardsAcct(5000.00, "REWARDS")
        }

        self.current_selected_account = None
        self.transaction_type = None

        self.amount_var = ctk.StringVar()
        self.account_name_var = ctk.StringVar()
        self.initial_balance_var = ctk.StringVar()
        self.account_type_var = ctk.StringVar(value="Standard")

        self.font_heading = ctk.CTkFont("Arial", 18, "bold")
        self.font_label = ctk.CTkFont("Arial", 12)
        self.font_button = ctk.CTkFont("Arial", 14, "bold")
        self.font_entry = ctk.CTkFont("Arial", 12)

        self.btn_color_primary = "#428bca"
        self.btn_hover_primary = "#3276b1"
        self.btn_color_success = "#5cb85c"
        self.btn_hover_success = "#4cae4c"
        self.btn_color_warning = "#f0ad4e"
        self.btn_hover_warning = "#eb9316"
        self.btn_color_danger = "#d9534f"
        self.btn_hover_danger = "#c9302c"
        self.btn_color_neutral = "#6c757d"
        self.btn_hover_neutral = "#5a6268"

        self._create_main_layout_containers()
        self._create_all_dynamic_screens()



    def _create_main_layout_containers(self):
        self.main_frame = ctk.CTkFrame(self.root, fg_color="#343a40", corner_radius=10)
        self.main_frame.pack(fill=ctk.BOTH, expand=True, padx=20, pady=20)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=3)

        self.status_display_var = ctk.StringVar(value="WELCOME! PLEASE INSERT YOUR CARD.")
        self.status_display_frame = ctk.CTkFrame(self.main_frame, fg_color="#495057", corner_radius=8)
        self.status_display_label = ctk.CTkLabel(
            self.status_display_frame, textvariable=self.status_display_var,
            font=ctk.CTkFont("Arial", 18, "bold"), text_color="#ffffff",
            wraplength=500, justify="center"
        )
        self.status_display_label.pack(fill=ctk.BOTH, expand=True, padx=15, pady=15)
        self.status_display_frame.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")

        self.content_frame = ctk.CTkFrame(self.main_frame, fg_color="#495057", corner_radius=8)
        self.content_frame.grid(row=1, column=0, pady=10, padx=10, sticky="nsew")
        self.content_frame.grid_columnconfigure(0, weight=1)

    def _create_all_dynamic_screens(self):
        self.screens = {}

        self.welcome_screen = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        self.screens['welcome'] = self.welcome_screen
        ctk.CTkButton(self.welcome_screen,
                      text="INSERT CARD",
                      command=print("Remind me later: insert card"),
                      font=self.font_button,
                      fg_color=self.btn_color_primary,
                      hover_color=self.btn_hover_primary).pack(pady=50)

        self.account_select_screen = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        self.screens['account_select'] = self.account_select_screen
        ctk.CTkLabel(self.account_select_screen,
                     text="CHOOSE ACCOUNT TYPE:",
                     font=self.font_heading,
                     text_color="#ffffff").pack(pady=15)

        account_type_buttons_info = [
            ("CHECKING", "CHECKING"),
            ("SAVINGS", "SAVINGS"),
            ("INTEREST REWARDS", "REWARDS"),
            ("CREATE NEW ACCOUNT", "NEW")
        ]
        for text, type_val in account_type_buttons_info:
            ctk.CTkButton(self.account_select_screen,
                          text=text,
                          command=print("Remind me later"),
                          font=self.font_button,
                          fg_color=self.btn_color_primary,
                          hover_color=self.btn_hover_primary).pack(fill=ctk.X, pady=4, padx=50)

        ctk.CTkButton(self.account_select_screen,
                      text="RETURN CARD / CANCEL",
                      command=print("Remind me later: return card/cancel"),
                      font=self.font_button,
                      fg_color=self.btn_color_danger,
                      hover_color=self.btn_hover_danger).pack(pady=20)