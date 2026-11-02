import customtkinter as ctk

class Exemplo_CTkCheckBox(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Exemplo de CTkCheckBox')
        self.geometry('400x300')
        self.checkbox_var = ctk.StringVar(value="desmarcado")
        checkbox = ctk.CTkCheckBox(master=self, text="Clique aqui", 
                                   command=self.checkbox_event, 
                                   variable=self.checkbox_var,
                                   onvalue="marcado", offvalue="desmarcado",
                                   width=200)
        checkbox.grid(row=0, column=0, pady=10, padx=10, sticky="w")
        self.label = ctk.CTkLabel(master=self, text=f"O checkbox está {self.checkbox_var.get()}.", 
                                  width=300, anchor="w")
        self.label.grid(row=1, column=0, pady=10, padx=10, sticky="w")

    def checkbox_event(self):
        self.label.configure(text=f"O checkbox está {self.checkbox_var.get()}.")

if __name__ == '__main__':
    app = Exemplo_CTkCheckBox()
    app.mainloop()