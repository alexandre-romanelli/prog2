import customtkinter as ctk

class Atividade1(ctk.CTk):
  def __init__(self):
    super().__init__()
    self.title("Atividade 1")
    self.geometry("600x200")

    self.label = ctk.CTkLabel(master=self, text="Data:")
    self.label.grid(row=1, column=0, padx=10, pady=10)
    ctk.CTkLabel(master=self, text="Ano").grid(row=0, column=1, padx=10, pady=10)
    ctk.CTkLabel(master=self, text="Mês").grid(row=0, column=2, padx=10, pady=10)
    ctk.CTkLabel(master=self, text="Dia").grid(row=0, column=3, padx=10, pady=10)

    self.ano_var = ctk.IntVar(master=self, value=2026)
    ctk.CTkEntry(master=self, textvariable=self.ano_var).grid(row=1, column=1, padx=10, pady=10)
    self.mes_var = ctk.StringVar(master=self, value="Janeiro")
    ctk.CTkOptionMenu(master=self, 
                      values=["Janeiro", "Fevereiro", "Março", 
                              "Abril", "Maio", "Junho", 
                              "Julho", "Agosto", "Setembro", 
                              "Outubro", "Novembro", "Dezembro"],
                              variable=self.mes_var,
                              command=self.atualizar_dias) \
                      .grid(row=1, column=2, padx=10, pady=10)
    self.dias_mes_31 = [i for i in range(1, 32)]
    self.dias_mes_30 = [i for i in range(1, 31)]
    self.dias_mes_29 = [i for i in range(1, 30)]
    self.dias_mes_28 = [i for i in range(1, 29)]

    self.dia_var = ctk.StringVar(master=self, value="01")
    self.dia = ctk.CTkOptionMenu(master=self, 
                                 values=[f"{i:02d}" for i in range(1, 32)],
                                 variable=self.dia_var)
    self.dia.grid(row=1, column=3, padx=10, pady=10)

    ctk.CTkButton(master=self, 
                  text="Exibir data", 
                  command=self.exibir_data) \
                  .grid(row=2, column=1, columnspan=3, padx=10, pady=10, sticky="w")

    self.label = ctk.CTkLabel(master=self, text="A data será exibida aqui.")
    self.label.grid(row=4, column=1, columnspan=3, padx=10, pady=10)

  def atualizar_dias(self, *args):
    mes = self.mes_var.get()
    if mes in ["Janeiro", "Março", "Maio", "Julho", "Agosto", "Outubro", "Dezembro"]:
        dias = self.dias_mes_31
    elif mes in ["Abril", "Junho", "Setembro", "Novembro"]:
        dias = self.dias_mes_30
    elif mes == "Fevereiro":
        ano = self.ano_var.get()
        # verifica se ano é bissexto
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            dias = self.dias_mes_29
        else:
            dias = self.dias_mes_28
    else:
        dias = []

    self.dia_var.set("01")
    self.dia.configure(values=[f"{i:02d}" for i in dias])
     
  def exibir_data(self):
    ano = self.ano_var.get()
    mes = self.mes_var.get()
    dia = self.dia_var.get()
    data_formatada = f"{dia}/{mes}/{ano}"
    self.label.configure(text=f"Data: {data_formatada}")

if __name__ == "__main__":
    app = Atividade1()
    app.mainloop()