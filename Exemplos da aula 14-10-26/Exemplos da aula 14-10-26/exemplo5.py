from tkinter import messagebox

messagebox.showinfo("Título", "Operação concluída!")
messagebox.showwarning("Aviso", "Cuidado!")
messagebox.showerror("Erro", "erro não encontrado!")

resposta = messagebox.askyesno("Sair", "Deseja sair?") #Temos um valor que é True ou False