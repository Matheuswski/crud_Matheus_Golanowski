import tkinter as tk
from tkinter import mensagebox
from crud import creat_user,read_users,update_user,delet_user

class CRUDApp:
    def __init__(self,root):
        self.root = root
        self.root.title("CRUD UsUARIOS")

        #Criação de WIDGETS
        self.create_widgets()

    def create_widgets(self):
        #Labels
        tk.Label(self.root,text="Nome:").grid(row=0, column=0)
        tk.Label(self.root,text="Telefone:").grid(row=1, column=0)
        tk.Label(self.root,text="Email:").grid(row=2, column=0)
        tk.Label(self.root,text="Usuario:").grid(row=3, column=0)
        tk.Label(self.root,text="Senha:").grid(row=4, column=0)

        tk.Label(self.root,text="User ID(for update/delete):").grid(row=5, column=0)

        #Cria as caixas para digitar os valores
        self.nome_entry = tk.Entry(self.root)
        self.telefone_entry = tk.Entry(self.root)
        self.email_entry = tk.Entry(self.root)
        self.usuario_entry = tk.Entry(self.root)
        self.senha_entry = tk.Entry(self.root)
        self.user_id_entry = tk.Entry(self.root)

        self.nome_entry.grid(row=0, column=1)
        self.telefone_entry.grid(row=1, column=1)
        self.email_entry.grid(row=2, column=1)
        self.usuario_entry.grid(row=3, column=1)
        self.senha_entry.grid(row=4, column=1)

        self.user_id_entry.grid(row=5, column=1)

        #Botoes do crud
        tk.Button(self.root,text="Criar Usuario", command=self.create_user).grid(row=6, column=0, collumnspan=1)
        tk.Button(self.root,text="Listar Usuario", command=self.create_user).grid(row=6, column=1, collumnspan=1)
        tk.Button(self.root,text="Alterar Usuario", command=self.create_user).grid(row=7, column=0, collumnspan=1)
        tk.Button(self.root,text="Excluir Usuario", command=self.create_user).grid(row=7, column=1, collumnspan=1)

    def create_user(self):
        nome = self.nome_entry.get()
        telefone = self.telefone_entry.get()
        email = self.email_entry.get()
        usuario = self.usuario_entry.get()
        senha = self.senha_entry.get()
        user_id = self.user_id_entry.get()

        if nome and telefone and email and usuario and senha:
            creat_user(nome,telefone,email,usuario,senha)
            self.nome_entry.delete(0,tk.END)
            self.telefone_entry.delete(0,tk.END)
            self.email_entry.delete(0,tk.END)
            self.usuario_entry.delete(0,tk.END)
            self.senha_entry.delete(0,tk.END)
            messagebox.showerror("susseso","usuario criado com sussesso")

        else:
            messagebox.showerror("erro","todos os campos sao obrigatorios")
    
    def read_users(self):
        users =read_users()
        self.text_area.delete(1.0,tk.END)
        for user in users:
            self.text_area.insert(tk.END,f"id: {user[0]},nome: {user[1]},telefone: {user[0]},email: {user[0]}\n")

    def update_user(self):
        user_id = self.user_id_entry.get()
        nome = self.nome_entry.get()
        telefone = self.telefone_entry.get()
        email = self.email_entry.get()
        usuario = self.usuario_entry.get()
        senha = self.senha_entry.get()

        if user_id and nome and telefone and email and usuario and senha:
            update_user(user_id,nome,telefone,email,usuario,senha)
            self.nome_entry.delete(0,tk.END)
            self.telefone_entry.delete(0,tk.END)
            self.email_entry.delete(0,tk.END)
            self.usuario_entry.delete(0,tk.END)
            self.senha_entry.delete(0,tk.END)
            messagebox.showerror("susseso","usuario alterado com sussesso")

        else:
            messagebox.showerror("erro","todos os campos sao obrigatorios")