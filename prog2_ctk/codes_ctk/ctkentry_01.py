import customtkinter as ctk
from tkinter import messagebox

class Exemplo_CTkEntry(ctk.CTk):
  def __init__(self):
    super().__init__()
    self.title('Exemplo CTkEntry')
    self.geometry('400x300')
    self.entry = ctk.CTkEntry(master=self, placeholder_text="Digite um texto...", width=300)
    self.entry.grid(row=0, column=0, pady=5, padx=5)
    botao = ctk.CTkButton(master=self, text="Exibir texto", command=self.exibir_nome)
    botao.grid(row=1, column=0, pady=5, padx=5, sticky="w")

  def exibir_nome(self):
    texto = self.entry.get()
    messagebox.showinfo(title='Texto', message=f'Texto digitado: {texto}')

if __name__ == '__main__':
  app = Exemplo_CTkEntry()
  app.mainloop()