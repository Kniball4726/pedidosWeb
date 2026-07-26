from PIL import ImageTk, Image

def leer_imagen(path, size):
    return ImageTk.PhotoImage(Image.open(path).resize(size, Image.Resampling.LANCZOS))


def centrar_ventana(ventana, aplicacion_ancho, aplicacion_largo):
    ventana.update_idletasks()
    panta_ancho = ventana.winfo_screenwidth()
    panta_largo = ventana.winfo_screenheight()
    x = max(0, int((panta_ancho - aplicacion_ancho) / 2))
    y = max(0, int((panta_largo - aplicacion_largo) / 2))
    ventana.geometry(f"{aplicacion_ancho}x{aplicacion_largo}+{x}+{y}")
    ventana.update_idletasks()
    return ventana.geometry()
