import tkinter as tk
janela=tk.Tk()
janela.title("Cadastro")

tk.Label(janela,text="Nome:").grid(row=0,column=0, padx=8,pady=8,sticky="e")
nome=tk.Entry(janela,width=28)

nome.grid(row=0,column=1,padx=8,pady=8)
tk.Label(janela,text="E-mail:").grid(row=1,column=0,padx=8,pady=8,sticky="e")

email=tk.Entry(janela,width=28)
email.grid(row=1,column=1,padx=8,pady=8)
tk.Button(janela,text="Enviar").grid(row=2,column=0,columnspan=2,pady=12)

janela.mainloop()