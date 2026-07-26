import tkinter as tk
import src.util.generic as utl


class MasterPanel:
    def __init__(self, usu):
        self.ventana = tk.Tk()
        self.ventana.title(f"Bienvenid@, {usu}")
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()
        self.ventana.geometry("%dx%d+0+0" % (w,h))
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(False, False)

        logo = utl.leer_imagen("src/assets/logo2.png", (200, 200))

        label = tk.Label(self.ventana, image=logo, bg="black")
        label.place(x=0, y=0, relwidth=1, relheight=1)

        """btn_cerrar = tk.Button(
            self.ventana,
            text="Cerrar",
            command=self.ventana.destroy,
            bg="#b22222",
            fg="white",
            relief="flat",
            padx=10,
            pady=5,
        )
        btn_cerrar.place(relx=0.98, rely=0.02, anchor="ne")
"""
        self.ventana.mainloop()
