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

posiciones = {
    "familiar": (310, 200),
    "calaverita": (50, 400),
    "flor": (250, 400),
    "vela": (450, 400),
    "pan": (600, 400),
    "cruz": (350, 50)
}

for nombre, imagen in imagenes.items():
    if imagen:
        tk.Label(root, image=imagen, bg="orange").place(x=posiciones[nombre][0], y=posiciones[nombre][1])

tk.Label(root, text="Altar de Día de Muertos", font=("Helvetica", 20), bg="orange", fg="purple").pack(pady=20)

root.mainloop()