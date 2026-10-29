import customtkinter

def button_callback():
    print("Botão clicado")

app = customtkinter.CTk()
app.geometry("500x200")

button = customtkinter.CTkButton(app, text="Botão de clicar", command=button_callback)
button.pack(padx=30, pady=30)

app.mainloop()