import customtkinter as ctk

class TelaPrincipal(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Tela Principal')
        self.geometry('300x200')
        self.resizable(True, False)
        self.build_gui()

    def build_gui(self):
        ctk.CTkButton(self, text="Abrir Formulário de Cadastro", command=self.abrir_formulario).pack(pady=20)
        self.entry_nome = ctk.CTkEntry(self, placeholder_text="Nome")
        self.entry_nome.pack(pady=5)
        self.entry_sobrenome = ctk.CTkEntry(self, placeholder_text="Sobrenome")
        self.entry_sobrenome.pack(pady=5)
        self.entry_email = ctk.CTkEntry(self, placeholder_text="E-mail")
        self.entry_email.pack(pady=5)

    def abrir_formulario(self):
        form = FormCadastro(master=self)
        form.grab_set()  # Impede interação com a janela principal enquanto o formulário estiver aberto

    def inserir(self, nome, sobrenome, email):
        self.entry_nome.set(nome)
        self.entry_sobrenome.set(sobrenome)
        self.entry_email.set(email)

class FormCadastro(ctk.CTkToplevel):
    def __init__(self, master=TelaPrincipal, **kwargs):
        super().__init__(master=master, **kwargs)
        self.parent = master
        self.title('Cadastro de usuário')
        self.geometry('450x170')
        self.resizable(True, False)
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

        ctk.CTkButton(self, 
                      text="Salvar",
                      command=self.salvar,
                      width=100).grid(row=3, 
                                      column=1,
                                      padx=6, 
                                      pady=6, 
                                      sticky='e')

    def salvar(self):
        nome = self.entry_nome.get()
        sobrenome = self.entry_sobrenome.get()
        email = self.entry_email.get()
        self.parent.inserir(nome, sobrenome, email)
        self.destroy()

if __name__ == '__main__':
    app = TelaPrincipal()
    app.mainloop()