import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        peso = float(entry_peso.get().replace(",","."))
        altura = float(entry_altura.get().replace(",","."))
        if peso <= 0 or altura <= 0:
            raise ValueError
        
        imc = peso / altura ** 2
        
    except ValueError:
        messagebox.showerror(
            "Erro","Digite peso e altura positivos e válidos."
        )
        return
    if imc < 18.5:
        classe = "Abaixo do peso"
    elif imc < 25:
        classe = "Peso normal"

janela=tk.Tk()
janela.title("CalculadoradeIMC")
janela.geometry("400x300")

tk.Label(janela,text="Peso(kg):").grid(row=0,column=0,padx=10,pady=10,sticky="e")
entry_peso=tk.Entry(janela); entry_peso.grid(row=0,column=1)

tk.Label(janela,text="Altura(m):").grid(row=1,column=0,padx=10,pady=10,sticky="e")
entry_altura=tk.Entry(janela);entry_altura.grid(row=1,column=1)

tk.Button(janela,text="Calcular",command=calcular).grid(row=2,column=0,columnspan=2,
pady=10)

resultado= tk.StringVar()

tk.Label(janela,textvariable=resultado,font=("Arial",11,"bold")).grid(row=3,column=0,
columnspan=2)

janela.mainloop()