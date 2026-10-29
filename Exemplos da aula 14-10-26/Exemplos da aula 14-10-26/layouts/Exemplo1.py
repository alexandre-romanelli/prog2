import tkinter as tk

janela=tk.Tk()
janela.title("Exemplo de layout")
janela.geometry("400x400")

tk.Label(janela, text = "\n Este é exemplo \n", bg="green").pack(
    side="top", fill="x", padx=25, pady=25
)

tk.Button(janela,text="Salvar").pack(pady=5)
tk.Button(janela,text="Cancelar").pack(pady=5)

janela.mainloop()