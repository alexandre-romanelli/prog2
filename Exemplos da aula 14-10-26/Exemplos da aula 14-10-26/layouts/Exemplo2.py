import tkinter as tk

janela=tk.Tk()
janela.geometry("420x260")
painel=tk.Frame(janela,bg="white")

painel.pack(fill="both",expand=True,padx=15,pady=15)
tk.Label(painel,text="Área principal",bg="lightblue").pack(
    fill="both",expand=True
)
tk.Button(janela,text="Fechar",command=janela.destroy).pack(pady=8)

janela.mainloop()