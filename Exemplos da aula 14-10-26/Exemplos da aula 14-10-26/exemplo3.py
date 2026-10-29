import tkinter as tk

janela = tk.Tk()
janela.title("Meu app")

rotulo = tk.Label(janela, text="Digite seu nome: ", font=("Arial", 14))
rotulo.pack(pady=5)

campo = tk.Entry(janela, width=30)
campo.pack(pady=5)

def saudar():
    texto = campo.get()
    rotulo.config(text=f"Olá, {texto}!")

tk.Button(janela, text="Saudar", command=saudar).pack(pady=5)
janela.mainloop()