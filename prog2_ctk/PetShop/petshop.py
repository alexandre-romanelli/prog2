import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

root = ctk.CTk()

style = ttk.Style()
# Use 'clam' or 'alt' because the default Windows/Mac themes 
# often override padding settings.
style.theme_use('alt') 

style.configure("Treeview.Heading", 
                font=("Arial", 8), 
                padding=(5, 4)) # (horizontal, vertical) padding
ttk.Style().configure('Treeview', rowheight=25)

colunas = ("Responsável", "Pet", "Gênero", "Espécie", "Raça", "Nascimento")
tree = ttk.Treeview(root, columns=(0, 1, 2, 3, 4, 5), show="headings", selectmode="browse")
tree.heading(0, text=colunas[0])
tree.heading(1, text=colunas[1])
tree.heading(2, text=colunas[2])
tree.heading(3, text=colunas[3])
tree.heading(4, text=colunas[4])
tree.heading(5, text=colunas[5])
tree.insert("", "end", values=("Value 1", "Value 2", "3", "4", "5", "6"))
tree.insert("", "end", values=("Value 1", "Value 2", "3", "4", "5", "6"))
tree.insert("", "end", values=("Value 1", "Value 2", "3", "4", "5", "6"))
tree.insert("", "end", values=("Value 1", "Value 2", "3", "4", "5", "6"))
tree.insert("", "end", values=("Value 1", "Value 2", "3", "4", "5", "6"))
tree.pack()

root.mainloop()