import customtkinter as ctk
from tkinter import messagebox

class Exemplo_CTkInputDialog(ctk.CTk):
  def __init__(self):
    super().__init__()
    self.title('Exemplo de CTkInputDialog')
    self.geometry('400x300')
    ctk.CTkButton(self, text='Exibir input dialog', 
                  command=self.mostrar) \
                    .grid(row=0, column=0, pady=20, padx=20)

  def mostrar(self):
    valor = ctk.CTkInputDialog(text='Digite um valor:').get_input()
    if valor is not None and valor != '':
      messagebox.showinfo(title='Input', message=f'Valor digitado: {valor}')
    else:
      messagebox.showinfo(title='Input', message='Nenhum valor digitado.')

if __name__ == '__main__':
  app = Exemplo_CTkInputDialog()
  app.mainloop()