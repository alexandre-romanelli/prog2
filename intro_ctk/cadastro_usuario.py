import customtkinter as ctk
from tkinter import ttk, messagebox

class TelaPrincipal(ctk.Ctk):
    tree_usuarios = None

    def __init__(self):
        super().__init__()
        self.title("Cadastro de usuário")
        self.geometry("600x400")
        self.resizable(False, False)
        