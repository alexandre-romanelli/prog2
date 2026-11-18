import customtkinter as ctk
from tkinter import ttk  # Importamos o Treeview do tkinter padrão

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistema de Gestão - Tabela CustomTkinter")
        self.geometry("600x400")

        # Configuração de layout da grade (grid)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        button_frame = ctk.CTkFrame(self)
        button_frame.grid(row=0, column=0, columnspan=4, padx=0, pady=0, sticky="ew")
        ctk.CTkButton(button_frame, text="Inserir", command=self.inserir).grid(row=0, column=0, padx=(10, 5), pady=10, sticky="w")
        ctk.CTkButton(button_frame, text="Alterar", command=self.alterar).grid(row=0, column=1, padx=(5, 5), pady=10, sticky="w")
        ctk.CTkButton(button_frame, text="Excluir", command=self.excluir).grid(row=0, column=2, padx=(5, 10), pady=10, sticky="w")

        # --- 2. Container para a Tabela (Frame) ---
        # Criamos um frame para segurar a tabela e permitir customização de bordas
        self.table_frame = ctk.CTkFrame(self)
        self.table_frame.grid(row=1, column=0, columnspan=4, padx=10, pady=(0, 10), sticky="nsew")
        self.table_frame.grid_columnconfigure(0, weight=1)
        self.table_frame.grid_rowconfigure(0, weight=1)

        # --- 3. Implementação do Treeview (Onde a mágica acontece) ---
        # Definindo as colunas
        columns = ("id", "nome", "preco", "estoque")
        self.tree = ttk.Treeview(self.table_frame, columns=columns, show="headings", selectmode="browse")

        # Definindo os cabeçalhos
        self.headings = {
            "id": "ID",
            "nome": "Nome do Produto",
            "preco": "Preço (R$)",
            "estoque": "Qtd Estoque"
        }
        for col, text in self.headings.items():
            self.tree.heading(col, text=text)
            self.tree.column(col, width=100, anchor="center")

        # Ajustando largura da coluna de nome (maior)
        self.tree.column("nome", width=200, anchor="w")

        # Adicionando Scrollbar para a tabela
        self.scrollbar = ctk.CTkScrollbar(self.table_frame, orientation="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        
        # Posicionamento do Treeview e Scrollbar
        self.tree.grid(row=0, column=0, columnspan=3, sticky="nsew")
        self.scrollbar.grid(row=0, column=3, sticky="ns")

        # --- 4. Dados de Exemplo ---
        dados = [
            ("1", "Teclado Mecânico", "250.00", "15"),
            ("2", "Mouse Gamer", "120.50", "30"),
            ("3", "Monitor 144Hz", "1200.00", "5"),
            ("4", "Headset USB", "180.00", "10"),
            ("5", "Mousepad XL", "50.00", "50"),
        ]

        for item in dados:
            self.tree.insert("", "end", values=item)

        # --- 5. Estilização (Crucial para combinar com CustomTkinter) ---
        self.style_treeview()

    def inserir(self):
        # Lógica para inserir um novo item na tabela
        print("Inserir item")

    def alterar(self):
        # Lógica para alterar o item selecionado na tabela
        selected_item = self.tree.selection()
        if selected_item:
            print(f"Alterar item: {self.tree.item(selected_item)['values']}")
        else:
            print("Nenhum item selecionado para alterar.")

    def excluir(self):
        # Lógica para excluir o item selecionado na tabela
        selected_item = self.tree.selection()
        if selected_item:
            print(f"Excluir item: {self.tree.item(selected_item)['values']}")
            self.tree.delete(selected_item)
        else:
            print("Nenhum item selecionado para excluir.")  

    def style_treeview(self):
        """Ajusta o estilo do Treeview para não parecer 'antigo' ao lado do CTk"""
        style = ttk.Style()
        style.theme_use("default")
        
        # Cores que combinam com o modo Dark do CustomTkinter
        bg_color = "#2b2b2b"  # Cor de fundo similar ao CTk
        fg_color = "white"
        selected_color = "#1f538d" # Azul padrão do CustomTkinter

        style.configure("Treeview",
                        background=bg_color,
                        foreground=fg_color,
                        fieldbackground=bg_color,
                        borderwidth=0,
                        rowheight=30)
        
        style.configure("Treeview.Heading",
                        background="#56738F",
                        foreground="black",
                        relief="flat", font=("Arial", 9, "bold"),
                        padding=(5, 5))

        style.map("Treeview",
                  background=[('selected', selected_color)],
                  foreground=[('selected', 'white')])

if __name__ == "__main__":
    app = App()
    app.mainloop()
