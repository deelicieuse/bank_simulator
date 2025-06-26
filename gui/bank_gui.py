import customtkinter as ctk
from tkinter import messagebox, simpledialog

class BankGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM SIMULATOR")
        self.root.geometry("600x700")
        self.root.resizable(False, False)

        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self._create_main_layout_containers()