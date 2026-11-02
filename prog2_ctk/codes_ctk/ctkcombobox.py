import customtkinter as ctk
from tkinter import messagebox

class Exemplo_CTkComboBox(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Exemplo de CTkComboBox')
        self.geometry('400x300')
        opcoes = ['Opcao 1', 'Opcao 2', 'Opcao 3', 'Opcao 4']
        self.combobox = ctk.CTkComboBox(self, values=opcoes, command=self.mostrar)
        self.combobox.grid(row=0, column=0, pady=10, padx=10)
        ctk.CTkButton(self, text='Exibir valor', 
                      command=lambda: self.mostrar(self.combobox.get())) \
                        .grid(row=1, column=0, pady=10, padx=10)

    def mostrar(self, valor_selecao):
        messagebox.showinfo(title='Selecao', message=f'Selecionada: {valor_selecao}')

if __name__ == '__main__':
    app = Exemplo_CTkComboBox()
    app.mainloop()