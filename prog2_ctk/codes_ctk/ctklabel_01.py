import customtkinter as ctk
class Exemplo_CTkLabel(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Exemplo de CTkLabel')
        self.geometry('400x300')
        label = ctk.CTkLabel(self,
                             text="Boa sorte!", 
                             font=("Arial", 20))
        label.pack(pady=20)

if __name__ == '__main__':
    app = Exemplo_CTkLabel()
    app.mainloop()