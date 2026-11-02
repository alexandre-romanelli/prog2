import customtkinter as ctk

class JanelaSecundaria(ctk.CTkToplevel):
  def __init__(self, master=None):
    super().__init__(master=master)
    self.title('Janela Secundária')
    self.geometry('300x200')
    label = ctk.CTkLabel(master=self, text="Esta é uma janela Toplevel.")
    label.grid(row=0, column=0, pady=20, padx=20)
    self.grab_set()

class Exemplo_CTkToplevel(ctk.CTk):
  def __init__(self):
    super().__init__()
    self.title('Janela Principal')
    self.geometry('400x300')
    botao = ctk.CTkButton(master=self, 
                          text="Abrir Toplevel", 
                          command=self.abrir_toplevel)
    botao.grid(row=0, column=0, pady=20, padx=20)

  def abrir_toplevel(self):
    toplevel = JanelaSecundaria(master=self)

if __name__ == '__main__':
  app = Exemplo_CTkToplevel()
  app.mainloop()