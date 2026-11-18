import customtkinter as ctk

class Exemplo_CTkCheckBox(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Exemplo de CTkCheckBox')
        self.geometry('400x300')
        self.checkbox_var = ctk.IntVar(value=0)
        checkbox = ctk.CTkCheckBox(master=self, text="Clique aqui", 
                                   command=self.checkbox_event, 
                                   variable=self.checkbox_var,
                                   onvalue=1, 
                                   offvalue=0,
                                   width=200)
        checkbox.grid(row=0, column=0, pady=10, padx=10, sticky="w")
        valor = self.checkbox_var.get()
        txt_valor = "marcado" if valor == 1 else "desmarcado"
        self.label = ctk.CTkLabel(master=self, text=f"O checkbox está {txt_valor}.", 
                                  width=300, anchor="w")
        self.label.grid(row=1, column=0, pady=10, padx=10, sticky="w")

    def checkbox_event(self):
        valor = self.checkbox_var.get()
        txt_valor = "marcado" if valor == 1 else "desmarcado"
        self.label.configure(text=f"O checkbox está {txt_valor}.")

if __name__ == '__main__':
    app = Exemplo_CTkCheckBox()
    app.mainloop()