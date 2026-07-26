import tkinter as tk
from tkinter.font import BOLD
import src.util.generic as utl

class FormLoginDesigner:

    def validar(self):
        pass

    def userRegister(self):
        pass
    
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('LogisticApp')
        self.ventana.config(bg='#000000')
        self.ventana.resizable(False, False)
        self.ventana.withdraw()
        utl.centrar_ventana(self.ventana, 700, 500)
        self.ventana.deiconify()
        logo = utl.leer_imagen("src/assets/logo2.png", (200, 200))
                
        #frame_logo
        frame_logo = tk.Frame(self.ventana, bd=0, width=300, relief=tk.FLAT, padx=0, pady=0, bg='#000000')
        frame_logo.pack(side='left', expand=tk.NO, fill=tk.BOTH)

        label = tk.Label(frame_logo, image=logo, bg='#000000')
        label.place(x=0, y=0, relwidth=1, relheight=1)

        #frame_form
        frame_form = tk.Frame(self.ventana, bd=0,width=300, relief=tk.FLAT, padx=0, pady=0, bg='#000000')
        frame_form.pack(side='right',expand=tk.YES,fill=tk.BOTH)

        #frame_form_top
        frame_form_top = tk.Frame(frame_form, height=50,bd=0,relief=tk.SOLID,bg='#000000')
        frame_form_top.pack(side='top',fill=tk.X)

        title = tk.Label(frame_form_top,text='Inicio de Sesión',font=('Times',30),fg='white',bg='#000000',pady=50)
        title.pack(expand=tk.YES,fill=tk.BOTH)

        #frame_form_fill
        frame_form_fill = tk.Frame(frame_form,height=50,bd=0,relief=tk.SOLID,bg='#000000')
        frame_form_fill.pack(side='bottom',expand=tk.YES,fill=tk.BOTH)

        txtUsuario=tk.Label(frame_form_fill,text="Usuario",font=('Times',14),fg='#fcfcfc',bg="#000000",anchor='nw')
        txtUsuario.pack(fill=tk.X,padx=20,pady=10)

        self.usuario = tk.Entry(frame_form_fill,font=('Times',14))
        self.usuario.pack(fill=tk.X,padx=20,pady=10)

        txtPassword=tk.Label(frame_form_fill,text="Usuario",font=('Times',14),fg='#fcfcfc',bg="#000000",anchor='nw')
        txtPassword.pack(fill=tk.X,padx=20,pady=10)

        self.password = tk.Entry(frame_form_fill,font=('Times',14))
        self.password.pack(fill=tk.X,padx=20,pady=10)
        self.password.config(show='*')

        btIngreso = tk.Button(frame_form_fill,text='Ingresar',font=('Times',15, BOLD),bd=0,fg='#000000',bg='red',command=self.validar)
        btIngreso.pack(fill=tk.X,padx=20,pady=20)

        btRegister = tk.Button(frame_form_fill,text='Registrar usuario',font=('Times',15),bd=0,fg='#3a7ff6',bg='#000000',command=self.userRegister)
        btRegister.pack(fill=tk.X,padx=20,pady=20)

        self.ventana.mainloop()


