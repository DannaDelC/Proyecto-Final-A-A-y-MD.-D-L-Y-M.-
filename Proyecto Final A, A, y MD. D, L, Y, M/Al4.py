import tkinter as tk          
from tkinter import ttk           

root = tk.Tk()
root.title("Matriz por regla de Cramer")
root.geometry("655x351")
root. configure(bg="#6f8073") 

style = ttk.Style()
style.configure("Cuestom.TFrame", background="#C8C6C9")

frame = ttk.Frame(root, padding="10 10 10 10", style="Cuestom.TFrame")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S,))

titulo = tk.Label(frame, text="Matriz por regla de Cramer", font=("Garamond", 24, "bold"), bg= "#C8C6C9", fg="black")
titulo.grid(column=0, row=0, sticky=tk.N, pady=(0, 10))

parrafo_texto= """La regla de Cramer es un método que utiliza determinantes para obtener las distintas soluciones de un sistema de ecuaciones lineales. Según sea el sistema se pueden aplicar el mismo método de dos formas distntintas.

Puede utilizarse cuando el determinante de la matriz A es distinto de cero, ya que las soluciones se obtienen dividiendo un determinante (ya veremos cuál) entre el determinante de la matriz A.

Si el determinante de la matriz A es cero no se podría utilizar este método, ya que dividir entre cero es imposible por la propia definición de la división, vamos que entre cero no se puede dividir.

Es importante destacar que este método de resolución de sistemas de ecuaciones lineales se debe utilizar una vez que se ha discutido el sistema para ver el número de soluciones de este y así poder aplicar el método apropiado.
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
    webbrowser.open_new("https://www.motyscience.com/bachillerato/2o-bachillerato/matematicas-ii-2o-bach/regla-de-cramer-resolucion-de-sistemas/")
enlace.bind("<Button-1>", abrir_url)

root.mainloop()



