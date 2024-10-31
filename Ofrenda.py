import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Altar de Día de Muertos")
root.geometry("800x600")
root.config(bg="orange")

def cargar_imagen(ruta, tamaño):
    try:
        img = Image.open(ruta).resize(tamaño, Image.LANCZOS)
        return ImageTk.PhotoImage(img)
    except:
        return None

imagenes = {
    "familiar": cargar_imagen("gojo.png", (180, 200)),
    "calaverita": cargar_imagen("calaverita.png", (150, 150)),
    "flor": cargar_imagen("flor.png", (120, 120)),
    "vela": cargar_imagen("vela3.png", (60, 150)),
    "pan": cargar_imagen("pan.png", (150, 150)),
    "cruz": cargar_imagen("cruz.png", (100, 150))
}