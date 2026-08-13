from services.user_service import UserService
import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox

class AppWindow(tk.Tk):
    def __init__(self, service: UserService) -> None:
        super().__init__()
        self.service = service

        self.title("Tkinter con POO + Capas")
        self.geometry("700x500")

         #Configuracion de filas y columnas
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.rowconfigure(5, weight=1)

        self.create_widget()

    def create_widget(self):
        self.render_entries()

        self.button_create_user = tk.Button(
            self, text="Ingresa un usuario", command=self.create_new_user)
        
        self.button_create_user.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        self.create_data_table()
        self.render_data_table()

    def render_entries(self):
        #NOMBRE
        label_fname = tk.Label(self, text="Ingresa tu nombre")
        label_fname.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.entry_fname = tk.Entry(self)
        self.entry_fname.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        #APELLIDO
        label_lname = tk.Label(self, text="Ingresa tu apellido")
        label_lname.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_lname = tk.Entry(self)
        self.entry_lname.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        #EDAD
        label_age = tk.Label(self, text="Ingresa tu edad")
        label_age.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_age = tk.Entry(self)
        self.entry_age.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

        #EMAIL
        label_email = tk.Label(self, text="Ingresa tu correo")
        label_email.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.entry_email = tk.Entry(self)
        self.entry_email.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

    def clear_entries(self):
        self.entry_fname.delete(0, "end")
        self.entry_lname.delete(0, "end")
        self.entry_age.delete(0, "end")
        self.entry_email.delete(0, "end")

        self.entry_fname.focus()

    def create_new_user(self):
        fname = self.entry_fname.get().strip()
        lname = self.entry_lname.get().strip()
        age = self.entry_age.get().strip()
        email = self.entry_email.get().strip()

        if not (fname and lname and age and email):
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
            return
        try:
            age = int(age)
        except ValueError:
            messagebox.showerror("Error", "La edad debe ser un numeroentero valido")
            return

        self.service.create_one(fname, lname, email, int(age))
        self.render_data_table()
        self.clear_entries()

    def create_data_table(self):
        self.tree = ttk.Treeview(self, columns=(
            "fname", "lname", "age", "email"), show="headings")

        self.tree.column("fname", anchor="center", width=120)
        self.tree.column("lname", anchor="center", width=120)
        self.tree.column("age", anchor="center", width=80)
        self.tree.column("email", anchor="center", width=200)

        self.tree.heading("fname", text="Nombre")
        self.tree.heading("lname", text="Apellido")
        self.tree.heading("age", text="Edad")
        self.tree.heading("email", text="Email")

        self.tree.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

    def render_data_table(self):
        users = self.service.find_all()

        for item in self.tree.get_children():
            self.tree.delete(item)

        for user in users:
            self.tree.insert("", "end", values=(
                user.fname, user.lname, user.age, user.email))