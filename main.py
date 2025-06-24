import tkinter as tk

from gui.bank_gui import BankGui

def main():
    root = tk.Tk()
    app = BankGui(root)
    root.mainloop()


if __name__ == '__main__':
    main()
