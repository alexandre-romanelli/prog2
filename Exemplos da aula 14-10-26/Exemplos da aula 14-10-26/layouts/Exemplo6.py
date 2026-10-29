import customtkinter as ctk
ctk.set_appearance_mode("system")
app=ctk.CTk()
app.title("Cadastro moderno")
app.geometry("420x300")
formulario=ctk.CTkFrame(app)

formulario.pack(fill="both",expand=True, padx=20,pady=20)
ctk.CTkLabel(formulario,text="Nome").grid(
row=0,column=0,padx=10, pady=10,sticky="e"
)

ctk.CTkEntry(formulario,placeholder_text=" Digite seu nome").grid(
row=0,column=1,padx=10, pady=10,sticky="ew"
)

formulario.grid_columnconfigure(1, weight=1)

app.mainloop()