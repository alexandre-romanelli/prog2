import customtkinter as ctk
from janela_registro_especie import JanelaRegistroEspecie
from janela_registro_raca import JanelaRegistroRaca

class JanelaPrincipalPetShop(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Pet Shop")
        self.geometry("200x200")

        # Botão para abrir a janela de cadastro de clientes
        botao_registro_especie = ctk.CTkButton(master=self, 
                                               text="Registro de Espécie", 
                                               command=self.abrir_registro_especie)
        botao_registro_especie.grid(row=0, column=0, pady=10, padx=20, sticky="ew")

        botao_registro_responsavel = ctk.CTkButton(master=self, 
                                                   text="Registro de Responsável", 
                                                   command=self.abrir_registro_responsavel)
        botao_registro_responsavel.grid(row=1, column=0, pady=10, padx=20, sticky="ew")

        botao_registro_raca = ctk.CTkButton(master=self, 
                                            text="Registro de Raça", 
                                            command=self.abrir_registro_raca)
        botao_registro_raca.grid(row=2, column=0, pady=10, padx=20, sticky="ew")

        botao_registro_pet = ctk.CTkButton(master=self, 
                                           text="Registro de Pet", 
                                           command=self.abrir_registro_pet)
        botao_registro_pet.grid(row=3, column=0, pady=10, padx=20, sticky="ew")


    def abrir_registro_especie(self):
        JanelaRegistroEspecie(master=self)


    def abrir_registro_responsavel(self):
        JanelaRegistroResponsavel(master=self)
        
    def abrir_registro_raca(self):
        JanelaRegistroRaca(master=self)


    def abrir_registro_pet(self):
        JanelaRegistroPet(master=self)

if __name__ == "__main__":
    app = JanelaPrincipalPetShop()
    app.mainloop()
