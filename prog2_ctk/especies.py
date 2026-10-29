import customtkinter as ctk
from tkinter import messagebox

class FormCadEspecie(ctk.CTk):
    def __init__(self, master=None):
        super().__init__(master)
        self.title('Cadastro de Espécie')
        self.geometry('400x320')
        self.resizable(True, False)
        self.build_gui()

    def build_gui(self):
        ctk.CTkLabel(self, text="Nome da Espécie", width=150, padx=6, pady=6, anchor="e").grid(row=0, column=0)
        self.entry_nome = ctk.CTkEntry(self, placeholder_text="Digite o nome da espécie")
        self.entry_nome.grid(row=0, column=1, sticky='ew', padx=6, pady=6)

        ctk.CTkLabel(self, text="Gênero", width=150, padx=6, pady=6, anchor="e").grid(row=1, column=0)
        self.entry_genero = ctk.CTkEntry(self, placeholder_text="Digite o gênero")
        self.entry_genero.grid(row=1, column=1, sticky='ew', padx=6, pady=6)

        ctk.CTkLabel(self, text="Família", width=150, padx=6, pady=6, anchor="e").grid(row=2, column=0)
        self.entry_familia = ctk.CTkEntry(self, placeholder_text="Digite a família")
        self.entry_familia.grid(row=2, column=1, sticky='ew', padx=6, pady=6)

        ctk.CTkLabel(self, text="Ordem", width=150, padx=6, pady=6, anchor="e").grid(row=3, column=0)
        self.entry_ordem = ctk.CTkEntry(self, placeholder_text="Digite a ordem")
        self.entry_ordem.grid(row=3, column=1, sticky='ew', padx=6, pady=6)

        ctk.CTkLabel(self, text="Classe", width=150, padx=6, pady=6, anchor="e").grid(row=4, column=0)
        self.entry_classe = ctk.CTkEntry(self, placeholder_text="Digite a classe")
        self.entry_classe.grid(row=4, column=1, sticky='ew', padx=6, pady=6)

        ctk.CTkLabel(self, text="Filo", width=150, padx=6, pady=6, anchor="e").grid(row=5, column=0)
        self.entry_filo = ctk.CTkEntry(self, placeholder_text="Digite o filo")
        self.entry_filo.grid(row=5, column=1, sticky='ew', padx=6, pady=6)

        ctk.CTkLabel(self, text="Reino", width=150, padx=6, pady=6, anchor="e").grid(row=6, column=0)
        self.entry_reino = ctk.CTkEntry(self, placeholder_text="Digite o reino")
        self.entry_reino.grid(row=6, column=1, sticky='ew', padx=6, pady=6)

        ctk.CTkButton(self, text="Salvar", width=100, command=self.salvar).grid(row=7, column=1, padx=6, pady=6, sticky='e')

    def salvar(self):
        nome = self.entry_nome.get()
        genero = self.entry_genero.get()
        familia = self.entry_familia.get()
        ordem = self.entry_ordem.get()
        classe = self.entry_classe.get()
        filo = self.entry_filo.get()
        reino = self.entry_reino.get()

        messagebox.showinfo("Salvar", f"Espécie: {nome}\nGênero: {genero}\nFamília: {familia}\nOrdem: {ordem}\nClasse: {classe}\nFilo: {filo}\nReino: {reino}")
if __name__ == '__main__':
    app = FormCadEspecie()
    app.mainloop()
