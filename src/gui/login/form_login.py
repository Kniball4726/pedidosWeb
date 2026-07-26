import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import src.util.generic as utl
from src.gui.login.form_login_designer import FormLoginDesigner 
from src.gui.master.form_master import MasterPanel

class FormLogin(FormLoginDesigner):

    def validar(self):
        usu = self.usuario.get().capitalize()
        passw = self.password.get()

        if usu == "Root" and passw == "1234":
            self.ventana.destroy()
            MasterPanel(usu)
        elif usu != "Root" and passw == "1234":
            messagebox.showwarning(title='Mensaje',message="Usuario incorrecto")
        elif usu == "Root" and passw != "1234":
            messagebox.showwarning(title='Mensaje',message="Contraseña incorrecta")
        elif usu == "" or passw == "":
            messagebox.showwarning(title='Mensaje',message='Debe llenar los campos de usuario y contraseña')
        else:
            messagebox.showwarning(title='Mensaje',message="Datos incorrectos")
        return usu

    def __init__(self):
        super().__init__()
   