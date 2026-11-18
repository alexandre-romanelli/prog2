import customtkinter as ctk

class TelaRegistroRaca(ctk.CTkToplevel):
  opcoes = ["Cão", "Gato", "Coelho"]

  def __init__(self, master, especie, raca, opcao):
    super().__init__()
    self.master = master
    self.opcao = opcao
    self.title = "Registro de raça"
    self.geometry("300x150")

    labelEspecie = ctk.CTkLabel(master=self, text="Espécie")
    labelEspecie.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    self.varOptionMenuEspecie = ctk.StringVar(master=self, value="")
    optionMenuEspecie = ctk.CTkOptionMenu(master=self, values=self.opcoes, variable=self.varOptionMenuEspecie)
    if especie != None:
      self.varOptionMenuEspecie.set(value=especie)
    optionMenuEspecie.grid(row=0, column=1, sticky="w")

    labelNomeRaca = ctk.CTkLabel(master=self, text="Raça")
    labelNomeRaca.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    
    self.entryNomeRaca = ctk.CTkEntry(master=self, width=200)
    if raca != None:
      self.entryNomeRaca.set(raca)
    self.entryNomeRaca.grid(row=1, column=1, sticky="w")

    frame = ctk.CTkFrame(master=self, height=40)
    frame.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="ew")
    
    buttonSalvar = ctk.CTkButton(master=frame, text="Salvar", command=self.salvar, width=80)
    buttonSalvar.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    
    buttonCancelar = ctk.CTkButton(master=frame, text="Cancelar", command=self.cancelar, width=80)
    buttonCancelar.grid(row=0, column=1, padx=0, pady=5, sticky="w")

    self.grab_set()

  def salvar(self):
    especie = self.varOptionMenuEspecie.get()
    raca = self.entryNomeRaca.get()
    if self.opcao == "novo":
      self.master.salvarNovo(especie, raca)
    elif self.opcao == "alterar":
      self.master.salvarAlteracao(especie, raca)
    self.destroy()

  def cancelar(self):
    self.destroy()

if __name__ == "__main__":
  app = TelaRegistroRaca()
  app.mainloop()
