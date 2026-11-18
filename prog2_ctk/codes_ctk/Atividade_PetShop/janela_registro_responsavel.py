import customtkinter as ctk

class JanelaRegistroResponsavel(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("Registro de Responsável")
        self.geometry("500x200")

        label_nome = ctk.CTkLabel(master=self, text="Nome:")
        label_nome.grid(row=0, column=0, pady=10, padx=10, sticky="w")
        self.entry_nome = ctk.CTkEntry(master=self)
        self.entry_nome.grid(row=0, column=1, pady=10, padx=10, sticky="we")

        label_telefone = ctk.CTkLabel(master=self, text="Telefone:")
        label_telefone.grid(row=1, column=0, pady=10, padx=10, sticky="w")
        self.entry_telefone = ctk.CTkEntry(master=self, width=120)
        self.entry_telefone.grid(row=1, column=1, pady=10, padx=10, sticky="w")

        label_endereco = ctk.CTkLabel(master=self, text="Endereço:")
        label_endereco.grid(row=2, column=0, pady=10, padx=10, sticky="w")
        self.entry_endereco = ctk.CTkEntry(master=self, width=400)
        self.entry_endereco.grid(row=2, column=1, pady=10, padx=10, sticky="w")

        frame_botoes = ctk.CTkFrame(master=self)
        frame_botoes.grid(row=3, column=1, columnspan=3, pady=20, padx=10, sticky="we")

        botao_salvar = ctk.CTkButton(master=frame_botoes, text="Registrar", command=self.salvar_responsavel)
        botao_salvar.grid(row=0, column=0, sticky="e")

        botao_cancelar = ctk.CTkButton(master=frame_botoes, text="Cancelar", command=self.destroy)
        botao_cancelar.grid(row=0, column=1, padx=10, sticky="w")

        self.grab_set()

    def salvar_responsavel(self):
        nome_responsavel = self.entry_nome.get()
        telefone_responsavel = self.entry_telefone.get()
        endereco_responsavel = self.entry_endereco.get()
        if nome_responsavel and telefone_responsavel:
            print("~ Responsável ~")
            print(f"  - Nome....: {nome_responsavel}")
            print(f"  - Telefone: {telefone_responsavel}")
            print(f"  - Endereço: {endereco_responsavel}")
            self.destroy()
        else:
            print("Por favor, insira o nome e o telefone do responsável.")

if __name__ == "__main__":
    app = JanelaRegistroResponsavel()
    app.mainloop()