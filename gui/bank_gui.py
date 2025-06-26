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