import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from tela_registro_raca import TelaRegistroRaca

class TelaTabelaRaca(ctk.CTkToplevel):
  def __init__(self, master):
    super().__init__()
    self.title("Tabela de raças")
    self.geometry("355x340")

    frame = ctk.CTkFrame(master=self, width=500, height=30)
    frame.grid(row=0, column=0, padx=15, pady=15, sticky="we")

    buttonNovo = ctk.CTkButton(master=frame, text="Novo", width=100, height=20, command=self.novo_registro)
    buttonNovo.grid(row=0, column=0, padx=5, pady=5)

    buttonAlterar = ctk.CTkButton(master=frame, text="Alterar", width=100, height=20, command=self.alterar)
    buttonAlterar.grid(row=0, column=1, padx=5, pady=5)

    buttonExcluir = ctk.CTkButton(master=frame, text="Excluir", width=100, height=20, command=self.excluir)
    buttonExcluir.grid(row=0, column=2, padx=5, pady=5)

    style = ttk.Style()
    #style.theme_use('clam')
    style.theme_use('alt') 

    style.configure("Treeview.Heading", font=("Arial", 10), padding=(5, 4))
    style.configure("Treeview", font=("Arial", 10))
    ttk.Style().configure('Treeview', rowheight=25)

    colunas = ("Espécie", "Raça")
    self.tree = ttk.Treeview(master=self, columns=(0, 1), show="headings", selectmode="browse")

    self.tree.heading(0, text=colunas[0])
    self.tree.heading(1, text=colunas[1])

    self.tree.column(0, width=150, anchor="center")
    self.tree.column(1, width=200, anchor="center")

    self.tree.insert("", "end", values=("Cão", "Vira-lata"))
    self.tree.insert("", "end", values=("Cão", "Basset hound"))
    self.tree.insert("", "end", values=("Cão", "Pastor alemão"))
    self.tree.insert("", "end", values=("Cão", "Shih tzu"))
    self.tree.insert("", "end", values=("Cão", "Lulu da Pomerânia"))
    self.tree.insert("", "end", values=("Cão", "Dálmata"))
    self.tree.insert("", "end", values=("Gato", "S.R.D."))
    self.tree.insert("", "end", values=("Gato", "Frajola"))
    self.tree.insert("", "end", values=("Gato", "Angorá"))
    self.tree.insert("", "end", values=("Gato", "Siamês"))
    self.tree.insert("", "end", values=("Gato", "Persa"))

    self.tree.grid(row=1, column=0, padx=5, pady=5)
    self.transient(master)

  def novo_registro(self):
    TelaRegistroRaca(self, None, "", "novo")

  def alterar(self):
    linhaSelecionada = self.tree.focus()
    itensSelecao = self.tree.item(linhaSelecionada)
    especie = itensSelecao.get("values")[0]
    raca = itensSelecao.get("values")[1]
    TelaRegistroRaca(self, especie, raca, "alterar")

  def excluir(self):
    opcao = tk.messagebox.askquestion(title="Confirmação", 
                                      message="Confirma exclusão?", 
                                      type=tk.messagebox.YESNO)
    if opcao == tk.messagebox.YES:
      itemAtual = self.tree.focus()
      self.tree.delete(itemAtual)

  def salvarNovo(self, especie: str, raca: str):
    self.tree.insert("", "end", values=(str(especie), str(raca)))

  def salvarAlteracao(self, especie, raca):
    itemAtual = self.tree.focus()
    self.tree.set(item=itemAtual, column=0, value=especie)
    self.tree.set(item=itemAtual, column=1, value=raca)

if __name__ == "__main__":
  app = TelaTabelaRaca()
  app.mainloop()