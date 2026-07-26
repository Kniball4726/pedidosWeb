import tkinter as tk
import src.util.generic as utl


class MasterPanel:
    def __init__(self, usu):
        self.ventana = tk.Tk()
        self.ventana.title(f"Bienvenid@, {usu}")
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()
        self.ventana.geometry("%dx%d+0+0" % (w,h))
        self.ventana.config(bg='#000000')
        self.ventana.resizable(False, False)

        logo = utl.leer_imagen("src/assets/logo2.png", (200, 200))

        label = tk.Label(self.ventana, image=logo, bg="#000000")
        label.place(x=0, y=0, relwidth=1, relheight=1)

        self.ventana.mainloop()
