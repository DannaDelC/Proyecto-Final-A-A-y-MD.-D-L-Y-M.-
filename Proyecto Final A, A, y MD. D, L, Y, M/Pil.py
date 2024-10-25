import tkinter as tk          
from tkinter import ttk           

root = tk.Tk()
root.title("Pillow")
root.geometry("655x330")
root. configure(bg="#6f8073")

style = ttk.Style()
style.configure("Cuestom.TFrame", background="#C8C6C9")

frame = ttk.Frame(root, padding="10 10 10 10", style="Cuestom.TFrame")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S,))

titulo = tk.Label(frame, text="Pillow", font=("Garamond", 24, "bold"), bg= "#C8C6C9", fg="black")
titulo.grid(column=0, row=0, sticky=tk.N, pady=(0, 10))

parrafo_texto= """Pillow es una variante (o fork) de la popular librería PIL (Python Image Library) que permite procesar con facilidad imágenes con Python 2.x/3.x. El proyecto lo inició Alex Clark cuando PIL se quedó sin desarrollo a finales del año 2009. Actualmente, Pillow es mantenido con la ayuda de otros colaboradores.

Con Pillow podemos consultar información básica de una imagen como su tamaño, el formato que tiene (jpg, png, gif, etc.), el tipo de imagen (bits/pixel, BN/color, etc.) y, también, es posible modificar su aspecto realizando operaciones para cambiar su tamaño, recortar un área, girar, aplicar filtros y efectos, convertir el tipo de imagen y su formato, etc.
"""
marco_3d = tk.Frame(frame, bg="#6f8073", borderwidth=4, relief="raised")
marco_3d.grid(column=0, row=1, padx=10, pady=10)


parrafo = tk.Text(marco_3d, font=("Helvetica", 12), wrap="word", bg="#8f9491", borderwidth=2, relief="solid", height=10, width=65)
parrafo.insert(tk.END, parrafo_texto)
parrafo.configure(state=tk.DISABLED)
parrafo.grid(column=0, row=0)

enlace = tk.Label(frame, text="Más información aquí", font=("Helvetica", 12), fg="#000000", bg="#8f9491",
                  cursor="hand2", borderwidth=2, relief="solid")
enlace.grid(column=0, row=2, sticky=tk.W, pady=(10, 10))

def abrir_url(event):
    import webbrowser
    webbrowser.open_new("https://python-para-impacientes.blogspot.com/2014/12/fundamentos-para-procesar-imagenes-con.html")
enlace.bind("<Button-1>", abrir_url)

root.mainloop()