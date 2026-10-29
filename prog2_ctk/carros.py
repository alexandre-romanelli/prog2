import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class Principal(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Tela Principal')
        self.geometry('300x300')
        self.resizable(True, False)
        self.build_gui()

    def build_gui(self):
        ctk.CTkButton(self, text="Abrir Formulário de Cadastro", command=self.abrir_formulario).pack(pady=20)
        self.entry_nome = ctk.CTkEntry(self, placeholder_text="Nome")
        self.entry_nome.pack(pady=5)
        self.entry_fabricante = ctk.CTkEntry(self, placeholder_text="Fabricante")
        self.entry_fabricante.pack(pady=5)
        self.entry_ano_fabricacao = ctk.CTkEntry(self, placeholder_text="Ano de Fabricação")
        self.entry_ano_fabricacao.pack(pady=5)
        self.entry_capacidade_cubica = ctk.CTkEntry(self, placeholder_text="Capacidade cúbica")
        self.entry_capacidade_cubica.pack(pady=5)
        self.entry_tipo_combustivel = ctk.CTkEntry(self, placeholder_text="Tipo de combustível")
        self.entry_tipo_combustivel.pack(pady=5)

    def abrir_formulario(self):
        form = FormCadastro(master=self)
        form.grab_set()  # Impede interação com a janela principal enquanto o formulário estiver aberto

    def inserir(self, nome, fabricante, ano_fabricacao, capacidade_cubica, tipo_combustivel):
        self.entry_nome.set(nome)
        self.entry_fabricante.set(fabricante)
        self.entry_ano_fabricacao.set(ano_fabricacao)
        self.entry_capacidade_cubica.set(capacidade_cubica)
        self.entry_tipo_combustivel.set(tipo_combustivel)

class FormCadastro(ctk.CTkToplevel):
    def __init__(self, master=Principal, **kwargs):
        super().__init__(master=master, **kwargs)
        self.parent = master
        self.title('Cadastro de Carro')
        self.geometry('450x300')
        self.resizable(True, False)
        self.build_gui()

    def build_gui(self):
        ctk.CTkLabel(self, text="Nome", width=100, padx=6, pady=6, anchor="e").grid(row=0, column=0)
        self.entry_nome = ctk.CTkEntry(self, placeholder_text="Digite o nome do carro", )
        self.entry_nome.grid(row=0, column=1, sticky='ew', padx=6, pady=6)

        ctk.CTkLabel(self, text="Fabricante", width=100, padx=6, pady=6, anchor="e").grid(row=1, column=0)
        self.entry_fabricante = ctk.CTkEntry(self, placeholder_text="Digite o fabricante")
        self.entry_fabricante.grid(row=1, column=1, sticky='ew', padx=6, pady=6)

        ctk.CTkLabel(self, text="Ano de Fabricação", width=100, padx=6, pady=6, anchor="e").grid(row=2, column=0)
        self.entry_ano_fabricacao = ctk.CTkEntry(self, width=300, placeholder_text="Digite o ano de fabricação")
        self.entry_ano_fabricacao.grid(row=2, column=1, sticky='ew', padx=6, pady=6)

        ctk.CTkLabel(self, text="Capacidade cúbica", width=100, padx=6, pady=6, anchor="e").grid(row=3, column=0)
        self.entry_capacidade_cubica = ctk.CTkEntry(self, placeholder_text="Digite a capacidade cúbica")
        self.entry_capacidade_cubica.grid(row=3, column=1, sticky='ew', padx=6, pady=6)

        ctk.CTkLabel(self, text="Tipo de combustível", width=100, padx=6, pady=6, anchor="e").grid(row=4, column=0)
        self.entry_tipo_combustivel = ctk.CTkEntry(self, placeholder_text="Digite o tipo de combustível")
        self.entry_tipo_combustivel.grid(row=4, column=1, sticky='ew', padx=6, pady=6)

        ctk.CTkButton(self, text="Salvar",
                      command=self.salvar, width=100).grid(row=5, column=1, padx=6, pady=6, sticky='e')

    def salvar(self):
        nome = self.entry_nome.get()
        fabricante = self.entry_fabricante.get()
        ano_fabricacao = self.entry_ano_fabricacao.get()
        capacidade_cubica = self.entry_capacidade_cubica.get()
        tipo_combustivel = self.entry_tipo_combustivel.get()
        self.parent.inserir(nome, fabricante, ano_fabricacao, capacidade_cubica, tipo_combustivel)
        self.destroy()  # Fecha o formulário após salvar
    
if __name__ == '__main__':
    app = Principal()
    app.mainloop()