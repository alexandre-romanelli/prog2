import tkinter as tk
janela=tk.Tk()
janela.title("Tela organizada")
janela.geometry("420x260")
cabecalho= tk.Frame(janela, bg="#dceeff")
cabecalho.pack(fill="x")
tk.Label(cabecalho,text="Sistema de Cadastro",
bg="#dceeff", font=("Arial", 20 ,"bold")).pack(pady=12)
conteudo=tk.Frame(janela, padx=15,pady=15)
conteudo.pack(fill="both",expand=True)
tk.Label(conteudo,text="Nome:").grid(row=0,column=0,sticky="w")
tk.Entry(conteudo).grid(row=0,column=1, padx=8, pady=6)
tk.Button(conteudo,text="Salvar").grid(row=1,column=1,sticky="e")
janela.mainloop()