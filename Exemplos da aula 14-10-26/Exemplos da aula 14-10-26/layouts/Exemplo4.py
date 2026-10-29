import tkinter as tk
janela=tk.Tk()
janela.geometry("400x250")
tk.Label(janela,text="Painel de controle").place(x=130,y=25)
tk.Button(janela,text="Ligar").place(x=90,y=90,width=90)
tk.Button(janela,text="Desligar").place(x=210,y=90,width=90)
tk.Label(janela,text="Centralizado").place(
relx=0.5,rely=0.5, anchor="center"
)
janela.mainloop()