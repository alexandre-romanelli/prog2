import customtkinter as ctk
from janela_registro_responsavel import JanelaRegistroResponsavel

class JanelaRegistroPet(ctk.CTkToplevel):
    lista_meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho",
                   "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    lista_meses_31_dias = ["Janeiro", "Março", "Maio", "Julho", "Agosto", "Outubro", "Dezembro"]
    lista_meses_30_dias = ["Abril", "Junho", "Setembro", "Novembro"]

    lista_31_dias = [f"{dia:02d}" for dia in range(1, 32)]
    lista_30_dias = [f"{dia:02d}" for dia in range(1, 31)]
    lista_29_dias = [f"{dia:02d}" for dia in range(1, 30)]
    lista_28_dias = [f"{dia:02d}" for dia in range(1, 29)]
    
    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("Registro de Pet")
        self.geometry("500x300")

        label_responsavel = ctk.CTkLabel(master=self, text="Responsável")
        label_responsavel.grid(row=0, column=0, pady=10, padx=10, sticky="w")
        self.combobox_responsavel = ctk.CTkComboBox(master=self, values=["Alexandre", "Adriano", "Gabriela"])
        self.combobox_responsavel.grid(row=0, column=1, pady=10, padx=10, sticky="we")
        botao_novo_responsavel = ctk.CTkButton(master=self, text="Novo", width=50, command=self.abrir_registro_responsavel)
        botao_novo_responsavel.grid(row=0, column=2, pady=10, padx=10, sticky="w")

        label_nome = ctk.CTkLabel(master=self, text="Nome")
        label_nome.grid(row=1, column=0, pady=10, padx=10, sticky="w")
        self.entry_nome = ctk.CTkEntry(master=self)
        self.entry_nome.grid(row=1, column=1, columnspan=3, pady=10, padx=10, sticky="we")

        label_genero = ctk.CTkLabel(master=self, text="Gênero")
        label_genero.grid(row=2, column=0, pady=10, padx=10, sticky="w")
        self.genero_var = ctk.StringVar(value="Fêmea")
        radioButton_femea = ctk.CTkRadioButton(master=self, text="Fêmea", value="Fêmea", variable=self.genero_var)
        radioButton_macho = ctk.CTkRadioButton(master=self, text="Macho", value="Macho", variable=self.genero_var)
        radioButton_femea.grid(row=2, column=1, pady=10, padx=10, sticky="w")
        radioButton_macho.grid(row=2, column=2, pady=10, padx=10, sticky="w")

        label_especie = ctk.CTkLabel(master=self, text="Espécie")
        label_especie.grid(row=3, column=0, pady=10, padx=10, sticky="w")
        self.combobox_especie = ctk.CTkComboBox(master=self, values=["Cachorro", "Gato"])
        self.combobox_especie.grid(row=3, column=1, pady=10, padx=10, sticky="we")
        botao_nova_especie = ctk.CTkButton(master=self, text="Nova", width=50, command=self.abrir_registro_especie)
        botao_nova_especie.grid(row=3, column=2, pady=10, padx=10, sticky="w")

        label_raca = ctk.CTkLabel(master=self, text="Raça")
        label_raca.grid(row=4, column=0, pady=10, padx=10, sticky="w")
        self.combobox_raca = ctk.CTkComboBox(master=self, values=["Labrador", "Poodle"])
        self.combobox_raca.grid(row=4, column=1, pady=10, padx=10, sticky="we")
        botao_nova_raca = ctk.CTkButton(master=self, text="Nova", width=50, command=self.abrir_registro_raca)
        botao_nova_raca.grid(row=4, column=2, pady=10, padx=10, sticky="w")

        label_nascimento = ctk.CTkLabel(master=self, text="Data nascimento")
        label_nascimento.grid(row=5, column=0, pady=10, padx=10, sticky="w")
        self.entry_ano = ctk.CTkEntry(master=self)
        self.entry_ano.grid(row=5, column=1, pady=10, padx=10, sticky="w")
        self.mes_var = ctk.StringVar(master=self)
        self.combobox_mes = ctk.CTkComboBox(master=self, values=self.lista_meses,
                                            variable=self.mes_var, 
                                            command=self.atualizar_dias)
        self.combobox_mes.grid(row=5, column=2, pady=10, padx=10, sticky="w")
        self.combobox_dia = ctk.CTkComboBox(master=self, values=self.lista_31_dias)
        self.combobox_dia.grid(row=5, column=3, pady=10, padx=10, sticky="w")

        frame_botoes = ctk.CTkFrame(master=self)
        frame_botoes.grid(row=6, column=1, columnspan=3, pady=20, padx=10, sticky="we")

        botao_salvar = ctk.CTkButton(master=frame_botoes, text="Registrar", command=self.salvar_pet)
        botao_salvar.grid(row=0, column=0)

        botao_cancelar = ctk.CTkButton(master=frame_botoes, text="Cancelar", command=self.destroy)
        botao_cancelar.grid(row=0, column=1)

        self.grab_set()

    def atualizar_dias(self):
        mes = self.mes_var.get()
        if mes in self.lista_meses_31_dias:
            self.combobox_dia.set(value=self.lista_31_dias)
        elif mes in self.lista_meses_30_dias:
            self.combobox_dia.set(value=self.lista_30_dias)

    def abrir_registro_especie(self):
        from janela_registro_especie import JanelaRegistroEspecie
        JanelaRegistroEspecie(master=self)

    def abrir_registro_raca(self):
        from janela_registro_raca import JanelaRegistroRaca
        JanelaRegistroRaca(master=self)

    def abrir_registro_responsavel(self):
        JanelaRegistroResponsavel(master=self)

    def salvar_pet(self):
        responsavel = self.combobox_responsavel.get()
        nome = self.entry_nome.get()
        genero = self.genero_var.get()
        especie = self.combobox_especie.get()
        raca = self.combobox_raca.get()
        if responsavel and nome and genero and especie and raca:
            print("~ Pet ~")
            print(f"  - Responsável: {responsavel}")
            print(f"  - Nome.......: {nome}")
            print(f"  - Gênero.....: {genero}")
            print(f"  - Espécie....: {especie}")
            print(f"  - Raça.......: {raca}")

if __name__ == "__main__":
    app = JanelaRegistroPet()
    app.mainloop()