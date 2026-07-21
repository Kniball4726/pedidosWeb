import tkinter as tk
import src.util.generic as utl


class MasterPanel:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Master Panel')
        self.ventana.update_idletasks()
        w = self.ventana.winfo_screenwidth()
        h = self.ventana.winfo_screenheight()
        self.ventana.geometry(f"{w}x{h}+0+0")
        self.ventana.attributes('-fullscreen', True)
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(False, False)

        logo = utl.leer_imagen("src/assets/logo2.png", (200, 200))

        label = tk.Label(self.ventana, image=logo, bg="red")
        label.place(x=0, y=0, relwidth=1, relheight=1)

        btn_cerrar = tk.Button(
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

        self.ventana.mainloop()
