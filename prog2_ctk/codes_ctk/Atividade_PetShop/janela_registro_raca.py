import customtkinter as ctk

class JanelaRegistroRaca(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("Registro de Raça")
        self.geometry("430x200")

        label_nome = ctk.CTkLabel(master=self, text="Nome da Raça:")
        label_nome.grid(row=0, column=0, pady=10, padx=10, sticky="w")
        self.entry_nome = ctk.CTkEntry(master=self)
        self.entry_nome.grid(row=0, column=1, columnspan=3, pady=10, padx=10, sticky="we")

        label_especie = ctk.CTkLabel(master=self, text="Espécie:")
        label_especie.grid(row=1, column=0, pady=10, padx=10, sticky="w")
        self.combobox_especie = ctk.CTkComboBox(master=self, values=["Cachorro", "Gato"])
        self.combobox_especie.grid(row=1, column=1, columnspan=2, pady=10, padx=10, sticky="w")

        botao_nova_especie = ctk.CTkButton(master=self, text="Nova", width=50, command=self.abrir_registro_especie)
        botao_nova_especie.grid(row=1, column=3, pady=10, padx=10, sticky="w")

        frame_botoes = ctk.CTkFrame(master=self, width=200)
        frame_botoes.grid(row=2, column=1, columnspan=3, pady=20, padx=0, sticky="w")

        botao_salvar = ctk.CTkButton(master=frame_botoes, text="Registrar", command=self.salvar_raca)
        botao_salvar.grid(row=0, column=0, sticky="e")

        botao_cancelar = ctk.CTkButton(master=frame_botoes, text="Cancelar", command=self.destroy)
        botao_cancelar.grid(row=0, column=1, padx=10, sticky="w")

        self.grab_set()

    def abrir_registro_especie(self):
        from janela_registro_especie import JanelaRegistroEspecie
        JanelaRegistroEspecie(master=self)

    def salvar_raca(self):
        nome_raca = self.entry_nome.get()
        nome_especie = self.combobox_especie.get()
        if nome_raca and nome_especie:
            print("~ Raça ~")
            print(f"  - Nome: {nome_raca}")
            print(f"  - Espécie: {nome_especie}")
            self.destroy()
        else:
            print("Por favor, insira o nome da raça.")

if __name__ == "__main__":
    app = JanelaRegistroRaca()
    app.mainloop()