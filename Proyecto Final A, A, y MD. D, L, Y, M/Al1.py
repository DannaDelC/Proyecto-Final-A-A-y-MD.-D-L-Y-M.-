import tkinter as tk 
from tkinter import ttk

root = tk.Tk() 
root.title("Definición de Matrices")
root.geometry("655x351")
root. configure(bg="#6f8073") 

style = ttk.Style()
style.configure("Cuestom.TFrame", background="#C8C6C9")

frame = ttk.Frame(root, padding="10 10 10 10", style="Cuestom.TFrame")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S,))

titulo = tk.Label(frame, text="Definición de Matrices", font=("Garamond", 24, "bold"), bg= "#C8C6C9", fg="black")
titulo.grid(column=0, row=0, sticky=tk.N, pady=(0, 10))

parrafo_texto = """Las matrices son un conjunto bidimensional de números o símbolos distribuidos de forma rectangular,  en líneas verticales y horizontales, de manera que sus elementos se organizan en filas y columnas. Sirven para describir  sistemas de ecuaciones lineales o diferenciales, así como para representar una aplicación lineal.

Toda matriz se representa por medio de una letra mayúscula, y sus elementos se reúnen entre dos paréntesis o corchetes, en letra minúscula. A su vez, tienen doble superíndice: el primero hace referencia a la fila y el segundo a la columna a la que pertenece.

Esta expresión matemática puede sumarse, multiplicarse y descomponerse, por lo que su uso es común en el álgebra lineal.
"""
marco_3d = tk.Frame(frame, bg="#6f8073", borderwidth=4, relief="raised")
marco_3d.grid(column=0, row=1, padx=10, pady=10)

parrafo = tk.Text(marco_3d, font=("Helvetica", 12), wrap="word", bg="#8f9491", borderwidth=2, relief="solid", height=12, width=65)
parrafo.insert(tk.END, parrafo_texto)
parrafo.configure(state=tk.DISABLED)
parrafo.grid(column=0, row=0)

enlace = tk.Label(frame, text="Más información aquí", font=("Helvetica", 12), fg="#000000", bg="#8f9491",
                  cursor="hand2", borderwidth=2, relief="solid")
enlace.grid(column=0, row=2, sticky=tk.W, pady=(10, 10))

def abrir_url(event):
    import webbrowser
    webbrowser.open_new("https://www.ferrovial.com/es/stem/matrices/")

enlace.bind("<Button-1>", abrir_url)

root.mainloop()