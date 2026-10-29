import customtkinter as ctk # biblioteca de GUI
from tkinter import messagebox # para exibir a mensagem

class TelaPrincipal(ctk.CTk):
    label_nome = None
    label_sobrenome = None
    label_email = None
    entry_nome = None
    entry_sobrenome = None
    entry_email = None
    button_salvar = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title('Cadastro de usuário')
        self.geometry('450x170')
        self.resizable(True, False)
        # self.configure(bg='black')
        self.build_gui()

    def build_gui(self):
        ctk.CTkLabel(self, text="Nome", width=100, padx=6, pady=6, anchor="e").grid(row=0, column=0)
        self.entry_nome = ctk.CTkEntry(self, placeholder_text="Digite o nome do usuário")
        self.entry_nome.grid(row=0, column=1, sticky='ew', padx=6, pady=6)

        ctk.CTkLabel(self, text="Sobrenome", width=100, padx=6, pady=6, anchor="e").grid(row=1, column=0)
        self.entry_sobrenome = ctk.CTkEntry(self, width=300, placeholder_text="Digite o sobrenome")
        self.entry_sobrenome.grid(row=1, column=1, padx=6, pady=6, sticky='ew')

        ctk.CTkLabel(self, text="E-mail", width=100, padx=6, pady=6, anchor="e").grid(row=2, column=0)
        self.entry_email = ctk.CTkEntry(self, placeholder_text="Digite o e-mail")
        self.entry_email.grid(row=2, column=1, padx=6, pady=6, sticky='ew')

        ctk.CTkButton(self, text="Salvar", width=100, command=self.salvar).grid(row=3, column=1, padx=6, pady=6, sticky='e')

    def salvar(self):
        nome = self.entry_nome.get()
        sobrenome = self.entry_sobrenome.get()
        email = self.entry_email.get()

        messagebox.showinfo("Salvar", nome + " - " + sobrenome + " - " + email)

if __name__ == '__main__':
    tela = TelaPrincipal()
    tela.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
