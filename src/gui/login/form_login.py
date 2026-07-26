import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import src.util.generic as utl
from src.gui.master.form_master import MasterPanel

class App:

    def validar(self):
        """usu = self.usuario.get()
        passw = self.password.get()

        if usu == "Root" and passw == "1234":
            self.ventana.destroy()
            MasterPanel(usu)
        elif usu != "Root":
            messagebox.showinfo("Usuario incorrecto",message="Mensaje")
        elif passw == "1234":
            messagebox.showinfo("Contraseña incorrecta",message="Mensaje")
        else:
            messagebox.showinfo("Datos incorrectos",message="Mensaje")
"""
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('LogisticApp')
        self.ventana.config(bg='black')
        self.ventana.resizable(False, False)
        self.ventana.withdraw()
        utl.centrar_ventana(self.ventana, 800, 500)
        self.ventana.deiconify()
        logo = utl.leer_imagen("src/assets/logo2.png", (200, 200))
                
        #frame_logo
        frame_logo = tk.Frame(self.ventana, bd=0, width=300, relief=tk.FLAT, padx=0, pady=0, bg='black')
        frame_logo.pack(side='left', expand=tk.NO, fill=tk.BOTH)
        label = tk.Label(frame_logo, image=logo, bg='black')
        label.place(x=0, y=0, relwidth=1, relheight=1)

        #frame_form
        frame_form = tk.Frame(self.ventana, bd=0,width=300, relief=tk.FLAT, padx=0, pady=0, bg='black')
        frame_form.pack(side='right',expand=tk.YES,fill=tk.BOTH)

        #frame_form_top
        frame_form_top = tk.Frame(frame_form, height=50,bd=0,relief=tk.SOLID,bg='black')
        frame_form_top.pack(side='top',fill=tk.X)
        title = tk.Label(frame_form_top,text='Inicio de Sesión',font=('Times',30),fg='white',bg='black',pady=50)
        title.pack(expand=tk.YES,fill=tk.BOTH)

        self.ventana.mainloop()
        


