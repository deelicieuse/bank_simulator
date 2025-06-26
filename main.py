import customtkinter as ctk
from gui.bank_gui import BankGUI

def main():
    root = ctk.CTk()
    app = BankGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()