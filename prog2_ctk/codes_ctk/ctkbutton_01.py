import customtkinter as ctk
from tkinter import messagebox

class Exemplo_CTkButton(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Exemplo de CTkButton')
        self.geometry('400x300')
        botao = ctk.CTkButton(self, 
                              text='Exibir Mensagem', 
                              command=self.mostrar_mensagem)
        botao.grid(row=0, column=0, pady=20, padx=20)
    
    def mostrar_mensagem(self):
        messagebox.showinfo(title='Mensagem', message='O botão foi clicado.')

if __name__ == '__main__':
    app = Exemplo_CTkButton()
    app.mainloop()