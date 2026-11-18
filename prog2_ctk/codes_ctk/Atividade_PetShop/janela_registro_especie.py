import customtkinter as ctk

class JanelaRegistroEspecie(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("Registro de Espécie")
        self.geometry("450x100")

        label_nome = ctk.CTkLabel(master=self, text="Nome da Espécie:")
        label_nome.grid(row=0, column=0, pady=10, padx=10)
        self.entry_nome = ctk.CTkEntry(master=self)
        self.entry_nome.grid(row=0, column=1, columnspan=2, pady=10, sticky="we")

        botao_salvar = ctk.CTkButton(master=self, text="Registrar", command=self.salvar_especie)
        botao_salvar.grid(row=1, column=1, pady=20)

        botao_cancelar = ctk.CTkButton(master=self, text="Cancelar", command=self.destroy)
        botao_cancelar.grid(row=1, column=2, pady=20, padx=10, sticky="w")

        self.grab_set()

    def salvar_especie(self):
        nome_especie = self.entry_nome.get()
        if nome_especie:
            print("~ Espécie ~")
            print(f"  - Nome: {nome_especie}")
            self.destroy()  # Fecha a janela após salvar
        else:
            print("Por favor, insira o nome da espécie.")

if __name__ == "__main__":
    app = JanelaRegistroEspecie()
    app.mainloop()