import customtkinter as ctk
import sqlite3
from tkinter import messagebox, ttk
from datetime import date

# Configurações de aparência
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("petshop.db")
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        # Tabelas base
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS responsavel (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT, telefone TEXT, endereco TEXT)""")
        
        self.cursor.execute("CREATE TABLE IF NOT EXISTS especie (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT UNIQUE)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS raca (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, especie_id INTEGER, FOREIGN KEY(especie_id) REFERENCES especie(id))")
        
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS pet (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            responsavel_id INTEGER, nome_pet TEXT, genero TEXT, 
            especie_id INTEGER, raca_id INTEGER, data_nasc DATE,
            FOREIGN KEY(responsavel_id) REFERENCES responsavel(id),
            FOREIGN KEY(especie_id) REFERENCES especie(id),
            FOREIGN KEY(raca_id) REFERENCES raca(id))""")
        
        # Inserir espécies e raças iniciais se estiver vazio
        self.cursor.execute("SELECT COUNT(*) FROM especie")
        if self.cursor.fetchone()[0] == 0:
            self.cursor.execute("INSERT INTO especie (nome) VALUES ('Cão'), ('Gato')")
            self.cursor.execute("INSERT INTO raca (nome, especie_id) VALUES ('Labrador', 1), ('Poodle', 1), ('Persa', 2), ('Siames', 2)")
        self.conn.commit()

    def execute(self, sql, params=()):
        self.cursor.execute(sql, params)
        self.conn.commit()
        return self.cursor

class AppMain(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.db = Database()
        self.title("Pet Shop - Controle Principal")
        self.geometry("900x500")

        # UI Principal
        self.label = ctk.CTkLabel(self, text="Lista de Animais Cadastrados", font=("Arial", 20, "bold"))
        self.label.pack(pady=10)

        # Treeview (Tabela) - Usando ttk para compatibilidade de tabelas
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", rowheight=25, font=('Arial', 10))
        
        self.tree = ttk.Treeview(self, columns=("Resp", "Pet", "Gen", "Esp", "Raça", "Idade"), show='headings')
        self.tree.heading("Resp", text="Responsável")
        self.tree.heading("Pet", text="Pet")
        self.tree.heading("Gen", text="Gênero")
        self.tree.heading("Esp", text="Espécie")
        self.tree.heading("Raça", text="Raça")
        self.tree.heading("Idade", text="Idade")
        self.tree.pack(expand=True, fill="both", padx=10, pady=10)

        # Botões de navegação
        btn_frame = ctk.CTkFrame(self)
        btn_frame.pack(fill="x", pady=10)

        ctk.CTkButton(btn_frame, text="Ver Responsáveis", command=self.abrir_janela_responsaveis).pack(side="left", padx=10)
        ctk.CTkButton(btn_frame, text="Cadastrar Pet", command=lambda: FormPet(self, self.db).abrir()).pack(side="left", padx=10)
        ctk.CTkButton(btn_frame, text="Atualizar Lista", command=self.carregar_pets).pack(side="left", padx=10)

        self.carregar_pets()

    def carregar_pets(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        sql = """SELECT r.nome, p.nome_pet, p.genero, e.nome, ra.nome, p.data_nasc 
                 FROM pet p
                 JOIN responsavel r ON p.responsavel_id = r.id
                 JOIN especie e ON p.especie_id = e.id
                 JOIN raca ra ON p.raca_id = ra.id"""
        res = self.db.execute(sql).fetchall()
        for row in res:
            # Cálculo de idade
            d1 = date.fromisoformat(row[5])
            today = date.today()
            idade = today.year - d1.year - ((today.month, today.day) < (d_ano := d1.month, d1.day)) # simplificado
            # Corrigindo cálculo de idade simples:
            idade = today.year - d1.year - ((today.month, today.day) < (d1.month, d1.day))
            
            self.tree.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4], f"{idade} anos"))

    def abrir_janela_responsaveis(self):
        JanelaResponsaveis(self, self.db).abrir()

# --- Janela de Tabela de Responsáveis ---
class JanelaResponsaveIS(ctk.CTkToplevel):
    # (Implementado dentro da classe principal para brevidade no exemplo)
    pass

class JanelaResponsaveis(ctk.CTkToplevel):
    def __init__(self, master, db):
        super().__init__(master)
        self.db = db
        self.title("Lista de Responsáveis")
        self.geometry("600x400")
        self.attributes("-topmost", True)

        self.tree = ttk.Treeview(self, columns=("ID", "Nome", "Tel", "End"), show='headings')
        for col in ("ID", "Nome", "Tel", "End"): self.tree.heading(col, text=col)
        self.tree.pack(expand=True, fill="both", padx=10, pady=10)

        btn_frame = ctk.CTkFrame(self)
        btn_frame.pack(fill="x", pady=5)

        ctk.CTkButton(btn_frame, text="Novo", width=70, command=lambda: FormResponsavel(self, db).abrir()).pack(side="left", padx=5)
        ctk.CTkButton(btn_frame, text="Alterar", width=70, command=self.alterar).pack(side="left", padx=5)
        ctk.CTkButton(btn_frame, text="Excluir", width=70, fg_color="red", command=self.excluir).pack(side="left", padx=5)

        self.carregar()

    def carregar(self):
        for item in self.tree.get_children(): self.tree.delete(item)
        res = self.db.execute("SELECT id, nome, telefone, endereco FROM responsavel").fetchall()
        for row in res: self.tree.insert("", "end", values=row)

    def alterar(self):
        selected = self.tree.selection()
        if not selected: return
        vals = self.tree.item(selected[0])['values']
        FormResponsavel(self, self.db, vals).abrir()

    def excluir(self):
        selected = self.tree.selection()
        if not selected: return
        if messagebox.askyesno("Confirmar", "Confirmar exclusão?"):
            id_resp = self.tree.item(selected[0])['values'][0]
            self.db.execute("DELETE FROM responsavel WHERE id=?", (id_resp,))
            self.carregar()

# --- Formulário Responsável ---
class FormResponsavel(ctk.CTkToplevel):
    def __init__(self, master, db, dados=None):
        super().__init__(master)
        self.db = db
        self.dados = dados
        self.title("Cadastro de Responsável")
        self.geometry("300x350")
        self.attributes("-topmost", True)

        ctk.CTkLabel(self, text="Nome:").pack()
        self.ent_nome = ctk.CTkEntry(self); self.ent_nome.pack()
        ctk.CTkLabel(self, text="Telefone:").pack()
        self.ent_tel = ctk.CTkEntry(self); self.ent_tel.pack()
        ctk.CTkLabel(self, text="Endereço:").pack()
        self.ent_end = ctk.CTkEntry(self); self.ent_end.pack()

        if dados:
            self.ent_nome.insert(0, dados[1]); self.ent_tel.insert(0, dados[2]); self.ent_end.insert(0, dados[3])

        btn_frame = ctk.CTkFrame(self)
        btn_frame.pack(pady=20)
        ctk.CTkButton(btn_frame, text="Registrar", command=self.registrar).pack(side="left", padx=5)
        ctk.CTkButton(btn_frame, text="Descartar", fg_color="gray", command=self.destroy).pack(side="left", padx=5)

    def abrir(self): self.deiconify()

    def registrar(self):
        nome, tel, end = self.ent_nome.get(), self.ent_tel.get(), self.ent_end.get()
        if self.dados: # Update
            self.db.execute("UPDATE responsavel SET nome=?, telefone=?, endereco=? WHERE id=?", (nome, tel, end, self.dados[0]))
        else: # Insert
            self.db.execute("INSERT INTO responsavel (nome, telefone, endereco) VALUES (?,?,?)", (nome, tel, end))
        messagebox.showinfo("Sucesso", "Salvo com sucesso!")
        self.master.carregar_pets()
        self.destroy()

# --- Formulário Pet ---
class FormPet(ctk.CTkToplevel):
    def __init__(self, master, db):
        super().__init__(master)
        self.db = db
        self.title("Cadastro de Pet")
        self.geometry("400x500")
        self.attributes("-topmost", True)

        # Carregar combos
        res_data = self.db.execute("SELECT id, nome FROM responsavel").fetchall()
        self.cb_resp = ctk.CTkComboBox(self, values=[f"{r[0]}-{r[1]}" for r in res_data])
        self.cb_resp.pack(pady=5)

        ctk.CTkLabel(self, text="Nome do Pet:").pack()
        self.ent_nome = ctk.CTkEntry(self); self.ent_nome.pack()

        ctk.CTkLabel(self, text="Gênero:").pack()
        self.cb_gen = ctk.CTkComboBox(self, values=["Macho", "Fêmea"]); self.cb_gen.pack()

        # Espécies
        esp_data = self.db.execute("SELECT nome FROM especie").fetchall()
        self.cb_esp = ctk.CTkComboBox(self, values=[e[0] for e in esp_data], command=self.on_esp_change)
        self.cb_esp.pack(pady=5)

        ctk.CTkLabel(self, text="Raça:").pack()
        self.cb_raca = ctk.CTkComboBox(self, values=[])
        self.cb_raca.pack(pady=5)

        ctk.CTkLabel(self, text="Data Nasc (AAAA-MM-DD):").pack()
        self.ent_data = ctk.CTkEntry(self); self.ent_data.pack()

        btn_frame = ctk.CTkFrame(self)
        btn_frame.pack(pady=20)
        ctk.CTkButton(btn_frame, text="Registrar", command=self.registrar).pack(side="left", padx=5)
        ctk.CTkButton(btn_frame, text="Descartar", fg_color="gray", command=self.destroy).pack(side="left", padx=5)

        self.on_esp_change("") # Init raças

    def on_esp_change(self, choice):
        # Busca raças baseadas na espécie selecionada
        res = self.db.execute("""SELECT r.nome FROM raca r 
                               JOIN especie e ON r.especie_id = e.id 
                               WHERE e.nome=?""", (choice,)).fetchall()
        self.cb_raca.configure(values=[r[0] for r in res])
        self.cb_raca.set(res[0][0] if res else "")

    def abrir(self): self.deiconify()

    def registrar(self):
        try:
            resp_id = self.cb_resp.get().split('-')[0]
            # Busca IDs de espécie e raça
            esp_name = self.cb_esp.get()
            esp_id = self.db.execute("SELECT id FROM especie WHERE nome=?", (esp_name,)).fetchone()[0]
            raca_name = self.cb_raca.get()
            raca_id = self.db.execute("SELECT id FROM raca WHERE nome=? AND especie_id=?", (raca_name, esp_id)).fetchone()[0]

            self.db.execute("""INSERT INTO pet (responsavel_id, nome_pet, genero, especie_id, raca_id, data_nasc) 
                            VALUES (?,?,?,?,?,?)""", 
                            (resp_id, self.ent_nome.get(), self.cb_gen.get(), esp_id, raca_id, self.ent_data.get()))
            messagebox.showinfo("Sucesso", "Pet cadastrado!")
            #                                                                                                                                               self.master.carlem_pets() # Error fix: master is AppMain
            self.master.carregar_pets()
            self.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Falha no cadastro: {e}")

if __name__ == "__main__":
    app = AppMain()
    app.mainloop()
