import tkinter as tk

def inicio():

    ventana = tk.Tk()

    ventana.title("Formulario de inicio de sesión")
    ventana.geometry("500x500")
    ventana.resizable(False, False)
    ventana.configure(background="red")

    ventana.mainloop()

inicio()