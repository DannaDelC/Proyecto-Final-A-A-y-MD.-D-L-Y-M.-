import tkinter as tk          
from tkinter import ttk           

root = tk.Tk()
root.title("Matrices Inversa")
root.geometry("655x351")
root. configure(bg="#6f8073") 

style = ttk.Style()
style.configure("Cuestom.TFrame", background="#C8C6C9")

frame = ttk.Frame(root, padding="10 10 10 10", style="Cuestom.TFrame")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S,))

titulo = tk.Label(frame, text="Matriz inversa", font=("Garamond", 24, "bold"), bg= "#C8C6C9", fg="black")
titulo.grid(column=0, row=0, sticky=tk.N, pady=(0, 10))

parrafo_texto= """En matemáticas, en particular en álgebra lineal, una matriz cuadrada A de orden n se dice que es invertible, no singular, no degenerada o regular si existe otra matriz cuadrada de orden n, llamada matriz inversa de A y denotada por A^{-1} si A⋅A^{-1}=A^{-1}⋅A=I_{n}, donde I_{n} es la matriz identidad de orden n y el producto utilizado es el producto de matrices usual.

Una matriz cuadrada no invertible se dice que es singular o degenerada. Una matriz es singular si y sólo si su determinante es nulo. La matriz singular A se caracteriza porque su multiplicación por la matriz columna X es igual a cero para algún X no nulo. El conjunto de estos vectores (y al subespacio vectorial formado por ellos) se llamará ker A (de kernel, núcleo en alemán), para una matriz invertible ker A es el vector nulo.

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
    webbrowser.open_new("https://es.wikipedia.org/wiki/Matriz_invertible")

enlace.bind("<Button-1>", abrir_url)

root.mainloop()


