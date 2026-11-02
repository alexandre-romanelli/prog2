import customtkinter as ctk
from tkinter import messagebox

class Exemplo_CTkOptionMenu(ctk.CTk):
  def __init__(self):
    super().__init__()
    self.title('Exemplo de CTkOptionMenu')
    self.geometry('400x300')
    opcoes = ['Opcao 1', 'Opcao 2', 'Opcao 3']
    self.optionmenu = ctk.CTkOptionMenu(self, values=opcoes,
                                        command=self.opcao_selecionada)
    self.optionmenu.grid(row=0, column=0, pady=10, padx=10)
    ctk.CTkButton(self, text='Exibir valor', 
                  command=lambda: self.opcao_selecionada(self.optionmenu.get())) \
                  .grid(row=1, column=0, pady=10, padx=10)

  def opcao_selecionada(self, valor):
    messagebox.showinfo(title='Selecao', message=f'Selecionada: {valor}')

if __name__ == '__main__':
  app = Exemplo_CTkOptionMenu()
  app.mainloop()