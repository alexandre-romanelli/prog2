import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class Exemplo_CTk(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Exemplo de CTk')
        self.geometry('400x300')

if __name__ == '__main__':
    app = Exemplo_CTk()
    app.mainloop()

    