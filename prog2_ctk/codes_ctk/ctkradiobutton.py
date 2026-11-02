import customtkinter as ctk
from tkinter import messagebox

class Exemplo_CTkRadioButton(ctk.CTk):
  def __init__(self):
    super().__init__()
    self.title('Exemplo de CTkRadioButton')
    self.geometry('400x300')
    self.int_var = ctk.IntVar(value=1)
    ctk.CTkRadioButton(
      master=self, text='Opcao 1', variable=self.int_var, value=1) \
      .grid(row=0, column=0, pady=10, padx=10, sticky="w")
    ctk.CTkRadioButton(
      master=self, text='Opcao 2', variable=self.int_var, value=2) \
      .grid(row=0, column=1, pady=10, padx=10, sticky="w")
    ctk.CTkButton(
      master=self, text='Exibir opcao selecionada', command=self.mostrar) \
      .grid(row=1, column=0, pady=10, padx=10, sticky="w")

  def mostrar(self):
    messagebox.showinfo(title='Selecao', message=f'Opcao {self.int_var.get()}.')

if __name__ == '__main__':
  app = Exemplo_CTkRadioButton()
  app.mainloop()