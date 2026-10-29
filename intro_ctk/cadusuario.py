# --------------------------------------------------------------
#  Formulário de cadastro (Nome, Sobrenome e E‑mail)
#  Biblioteca: customtkinter
# --------------------------------------------------------------

import customtkinter as ctk          # pip install customtkinter
from tkinter import messagebox       # para exibir a mensagem

# ------------------- Configurações globais -------------------
ctk.set_appearance_mode("dark")      # "light", "dark" ou "system"
ctk.set_default_color_theme("blue")  # opções: blue, green, dark-blue, etc.

class App(ctk.CTk):
    """Janela principal do aplicativo."""
    def __init__(self):
        super().__init__()

        self.title("Cadastro de Usuário")
        self.geometry("350x280")           # tamanho inicial da janela
        self.resizable(False, False)       # não permite redimensionar

        # ---------- Campo Nome ----------
        ctk.CTkLabel(self, text="Nome:").grid(row=0, column=0,
                                              padx=20, pady=(20, 5),
                                              sticky='w')
        self.entry_nome = ctk.CTkEntry(
            self,
            placeholder_text="Digite o nome"
        )
        self.entry_nome.grid(row=1, column=0,
                             padx=20, pady=5, sticky='ew')

        # ---------- Campo Sobrenome ----------
        ctk.CTkLabel(self, text="Sobrenome:").grid(row=2, column=0,
                                                   padx=20, pady=(15, 5),
                                                   sticky='w')
        self.entry_sobrenome = ctk.CTkEntry(
            self,
            placeholder_text="Digite o sobrenome"
        )
        self.entry_sobrenome.grid(row=3, column=0,
                                  padx=20, pady=5, sticky='ew')

        # ---------- Campo E‑mail ----------
        ctk.CTkLabel(self, text="E-mail:").grid(row=4, column=0,
                                                padx=20, pady=(15, 5),
                                                sticky='w')
        self.entry_email = ctk.CTkEntry(
            self,
            placeholder_text="Digite o e‑mail"
        )
        self.entry_email.grid(row=5, column=0,
                              padx=20, pady=5, sticky='ew')

        # ---------- Botão Salvar ----------
        ctk.CTkButton(self, text="Salvar", command=self.salvar).grid(
            row=6, column=0,
            padx=20, pady=(25, 10),
            sticky='e'
        )

        # Permite que o widget de entrada expanda horizontalmente
        self.columnconfigure(0, weight=1)

    def salvar(self):
        """Coleta os dados e exibe uma mensagem com o nome digitado."""
        nome = self.entry_nome.get().strip()
        if not nome:
            messagebox.showwarning("Campo obrigatório", "Por favor, digite seu nome.")
            return

        # Você pode usar os outros campos se precisar
        sobrenome = self.entry_sobrenome.get().strip()
        email = self.entry_email.get().strip()

        msg = f"Nome digitado: {nome}"
        if sobrenome:
            msg += f"\nSobrenome: {sobrenome}"
        if email:
            msg += f"\nE‑mail: {email}"

        messagebox.showinfo("Dados salvos", msg)

# ---------------------- Execução -----------------------------
if __name__ == "__main__":
    app = App()
    app.mainloop()
