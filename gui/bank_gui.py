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

    def _placeholder_handler(self):
        print("Button pressed (not yet implemented)")

    def _create_all_dynamic_screens(self):
        self.screens = {}

        self.welcome_screen = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        self.screens['welcome'] = self.welcome_screen
        ctk.CTkButton(self.welcome_screen,
                      text="INSERT CARD",
                      command=self._placeholder_handler(),
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
                          command=self._placeholder_handler(),
                          font=self.font_button,
                          fg_color=self.btn_color_primary,
                          hover_color=self.btn_hover_primary).pack(fill=ctk.X, pady=4, padx=50)

        ctk.CTkButton(
            self.account_select_screen,
            text="RETURN CARD / CANCEL",
            command=self._placeholder_handler(),
            font=self.font_button,
            fg_color=self.btn_color_danger,
            hover_color=self.btn_hover_danger
        ).pack(pady=20)

        self.transaction_menu_screen = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        self.screens['transaction_menu'] = self.transaction_menu_screen
        ctk.CTkLabel(self.transaction_menu_screen, text="SELECT TRANSACTION:", font=self.font_heading, text_color="#ffffff").pack(pady=15)
        transaction_buttons_info = [
            ("VIEW BALANCE", self._placeholder_handler()),
            ("DEPOSIT FUNDS", lambda: self._placeholder_handler("deposit")),
            ("WITHDRAW CASH", lambda: self._placeholder_handler("withdraw")),
            ("TRANSFER CREDITS", lambda: self._placeholder_handler("transfer"))
        ]
        for text, command in transaction_buttons_info:
            ctk.CTkButton(
                self.transaction_menu_screen,
                text=text, command=command,
                font=self.font_button,
                fg_color=self.btn_color_primary,
                hover_color=self.btn_hover_primary
            ).pack(fill=ctk.X, pady=4, padx=50)

        ctk.CTkButton(
            self.transaction_menu_screen,
            text="RETURN CARD / CANCEL",
            command=self._placeholder_handler(),
            font=self.font_button,
            fg_color=self.btn_color_danger,
            hover_color=self.btn_hover_danger
        ).pack(pady=20)

        self.post_transaction_screen = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        self.screens['post_transaction'] = self.post_transaction_screen
        ctk.CTkButton(
            self.post_transaction_screen,
            text="DO ANOTHER TRANSACTION",
            command=self._placeholder_handler(),
            font=self.font_button,
            fg_color=self.btn_color_primary,
            hover_color=self.btn_hover_primary
        ).pack(pady=10)
        self.receipt_button = ctk.CTkButton(
            self.post_transaction_screen,
            text="PRINT RECEIPT",
            command=self._placeholder_handler(),
            font=self.font_button,
            fg_color=self.btn_color_success,
            hover_color=self.btn_hover_success
        )
        self.receipt_button.pack(pady=10)
        ctk.CTkButton(
            self.post_transaction_screen,
            text="RETURN CARD / FINISH",
            command=self._placeholder_handler(),
            font=self.font_button,
            fg_color=self.btn_color_danger,
            hover_color=self.btn_hover_danger
        ).pack(pady=20)

        self.create_account_screen = ctk.CTkFrame(self.content_frame, fg_color="#495057", corner_radius=8)
        self.screens['create_account'] = self.create_account_screen
        ctk.CTkLabel(self.create_account_screen, text="ENTER NEW ACCOUNT DETAILS", font=self.font_heading,
                     text_color="#ffffff").pack(pady=10)

        input_grid_frame = ctk.CTkFrame(self.create_account_screen, fg_color="transparent")
        input_grid_frame.pack(fill=ctk.X, pady=5)
        input_grid_frame.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(input_grid_frame,
                     text="ACCOUNT NAME:",
                     text_color="#ffffff",
                     font=self.font_label
                     ).grid(row=0, column=0, padx=5, pady=5, sticky="w")
        ctk.CTkEntry(
            input_grid_frame,
            textvariable=self.account_name_var,
            font=self.font_entry,
            text_color="#000000",
             fg_color="#e0e0e0"
        ).grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        ctk.CTkLabel(
            input_grid_frame,
            text="STARTING BALANCE ($):",
            text_color="#ffffff",
            font=self.font_label
        ).grid(row=1, column=0, padx=5, pady=5, sticky="w")
        ctk.CTkEntry(input_grid_frame,
                     textvariable=self.initial_balance_var,
                     font=self.font_entry,
                     text_color="#000000",
                     fg_color="#e0e0e0"
                     ).grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        type_frame = ctk.CTkFrame(self.create_account_screen, fg_color="transparent")
        type_frame.pack(pady=10)
        ctk.CTkLabel(type_frame,
                     text="ACCOUNT TYPE:",
                     text_color="#ffffff",
                     font=self.font_label
                     ).pack(side=ctk.TOP,pady=5)
        ctk.CTkRadioButton(
            type_frame,
            text="STANDARD",
            variable=self.account_type_var,
            value="Standard",
            font=self.font_label,
            text_color="#ffffff",
            fg_color=self.btn_color_primary,
            hover_color=self.btn_hover_primary
        ).pack(side=ctk.LEFT, padx=10)
        ctk.CTkRadioButton(
            type_frame,
            text="INTEREST REWARDS",
            variable=self.account_type_var,
            value="Interest",
            font=self.font_label,
            text_color="#ffffff",
            fg_color=self.btn_color_primary,
            hover_color=self.btn_hover_primary
        ).pack(side=ctk.LEFT, padx=10)
        ctk.CTkRadioButton(
            type_frame,
            text="SAVINGS (W/ FEE)",
            variable=self.account_type_var,
            value="Savings",
            font=self.font_label,
            text_color="#ffffff",
            fg_color=self.btn_color_primary,
            hover_color=self.btn_hover_primary
        ).pack(side=ctk.LEFT, padx=10)

        ctk.CTkButton(
            self.create_account_screen,
            text="CREATE ACCOUNT",
            command=self.create_account,
            font=self.font_button,
            fg_color=self.btn_color_success,
            hover_color=self.btn_hover_success
        ).pack(fill=ctk.X, pady=5)
        ctk.CTkButton(
            self.create_account_screen,
            text="<< BACK TO ACCOUNT SELECTION",
            command=self._show_account_selection_screen,
            font=self.font_button,
            fg_color=self.btn_color_neutral,
            hover_color=self.btn_hover_neutral
        ).pack(fill=ctk.X, pady=10)

    def _hide_all_screens(self):
        for screen in self.screens.values():
            screen.pack_forget()

    def _show_screen(self, screen_to_show):
        self._hide_all_screens()
        screen_to_show.pack(fill=ctk.BOTH, expand=True)

    def _update_status(self, message):
        self.status_display_var.set(message.upper())

    def _clear_inputs(self):
        self.amount_var.set("")
        self.account_name_var.set("")
        self.initial_balance_var.set("")
        self.account_type_var.set("Standard")

    def _return_card_and_reset(self):
        self.current_selected_account = None
        self.transaction_type = None
        self._clear_inputs()
        self._update_status("THANK YOU! CARD EJECTED. HAVE A NICE DAY.")
        self.root.after(2000, lambda: self._show_screen(self.welcome_screen))

    def _show_account_selection_screen(self):
        self._clear_inputs()
        self._update_status("PLEASE SELECT YOUR ACCOUNT TYPE.")
        self._show_screen(self.account_select_screen)

    def _show_create_account_screen(self, *args):
        self._clear_inputs()
        self._update_status("ENTER NEW ACCOUNT DETAILS.")
        self._show_screen(self.create_account_screen)

    def _show_transaction_menu(self):
        if self.current_selected_account:
            self._update_status(
                f"ACCOUNT: {self.current_selected_account.name.upper()}\n"
                f"BALANCE: ${self.current_selected_account.get_balance():.2f}\n\n"
                f"SELECT TRANSACTION:"
            )
            self._show_screen(self.transaction_menu_screen)
        else:
            self._update_status("ERROR: NO ACCOUNT SELECTED. PLEASE SELECT AN ACCOUNT.")
            self._show_account_selection_screen()

    def _show_transaction_input(self, transaction_type):
        if not self.current_selected_account:
            self._update_status("ERROR: NO ACCOUNT SELECTED.")
            self._show_account_selection_screen()
            return

        self.transaction_type = transaction_type
        self._update_status(
            f"{transaction_type.upper()} OPERATION\n"
            f"ACCOUNT: {self.current_selected_account.name}\n"
            f"BALANCE: ${self.current_selected_account.get_balance():.2f}\n\n"
            f"ENTER AMOUNT:"
        )
        self.perform_transaction_button.configure(text=f"PERFORM {transaction_type.upper()}")
        self.amount_var.set("")
        self._show_screen(self.transaction_input_screen)

    def _show_post_transaction_screen(self, display_receipt_button=True):
        if display_receipt_button:
            self.receipt_button.pack(pady=10)
        else:
            self.receipt_button.pack_forget()
        self._show_screen(self.post_transaction_screen)

    def _select_account_type(self, acc_type):
        if acc_type == "NEW":
            self._show_create_account_screen()
            return

        selected_acc_name = acc_type
        if selected_acc_name in self.accounts:
            self.current_selected_account = self.accounts[selected_acc_name]
            self._update_status(
                f"{selected_acc_name.upper()} ACCOUNT SELECTED. "
                f"BALANCE: ${self.current_selected_account.get_balance():.2f}"
            )
            self._show_transaction_menu()
        else:
            messagebox.showerror("Account Not Found", f"No existing account of type '{acc_type.upper()}' found.\n\nPlease create a new account or select another type.")
            self._update_status(f"ERROR: ACCOUNT TYPE '{acc_type}' NOT FOUND.")
            self._show_account_selection_screen()

    def create_account(self):
        name = self.account_name_var.get().strip().upper()
        balance_str = self.initial_balance_var.get().strip()
        account_type = self.account_type_var.get()

        if not name:
            messagebox.showerror("Input Error", "Account name cannot be empty!")
            self._update_status("ACCOUNT NAME CANNOT BE EMPTY!")
            return
        if name in self.accounts:
            messagebox.showerror("Duplicate Account", f"Account '{name}' already exists!")
            self._update_status(f"ACCOUNT '{name}' ALREADY EXISTS!")
            return
        try:
            initial_balance = float(balance_str)
            if initial_balance < 0:
                raise ValueError("Negative balance not allowed.")
        except ValueError:
            messagebox.showerror("Invalid Balance", "Enter a valid non-negative number.")
            self._update_status("INVALID BALANCE.")
            return

        try:
            if account_type == "Standard":
                acct = BankAccount(initial_balance, name)
            elif account_type == "Interest":
                acct = InterestRewardsAcct(initial_balance, name)
            elif account_type == "Savings":
                acct = SavingsAcct(initial_balance, name)
            else:
                acct = BankAccount(initial_balance, name)

            self.accounts[name] = acct
            messagebox.showinfo("Account Created", f"'{name}' created with ${initial_balance:.2f}!")
            self._update_status(f"ACCOUNT '{name}' CREATED!")
            self._clear_inputs()
            self._show_account_selection_screen()
        except Exception as error:
            messagebox.showerror("Error", f"Account creation failed: {error}")
            self._update_status(f"CREATION FAILED: {error}")

    def _perform_current_transaction(self):
        if self.transaction_type == "deposit":
            self.perform_deposit()
        elif self.transaction_type == "withdraw":
            self.perform_withdraw()
        elif self.transaction_type == "transfer":
            self.perform_transfer()
        else:
            messagebox.showerror("Error", "Unknown transaction type.")
            self._update_status("UNKNOWN TRANSACTION TYPE.")
            self._show_transaction_menu()











