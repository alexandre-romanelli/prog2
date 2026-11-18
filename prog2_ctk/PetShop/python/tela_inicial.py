import customtkinter as ctk
from tela_tabela_raca import TelaTabelaRaca

class TelaInicial(ctk.CTk):
  def __init__(self):
    super().__init__()
    self.title("Pet Shop")
    self.geometry("400x500")
    ctk.CTkButton(master=self, width=150, height=30, 
                  text="Cadastro de raças", 
                  command=self.abrir_cadastro_raca).grid(row=0, column=0, 
                                                         padx=10, pady=10)
    self.grab_set()

  def abrir_cadastro_raca(self):
    TelaTabelaRaca()

if __name__ == "__main__":
  app = TelaInicial()
  app.mainloop()
