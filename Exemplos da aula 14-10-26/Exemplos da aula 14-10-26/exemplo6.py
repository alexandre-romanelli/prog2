import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.title("Exemplo 6")
janela.geometry("500x250")

combo = ttk.Combobox(janela, values=["Python", "Dart", "JavaScript"], state="readonly")
combo.current(0)
combo.pack(pady=20)

print(combo.get())

janela.mainloop()