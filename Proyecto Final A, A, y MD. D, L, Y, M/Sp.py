import tkinter as tk          
from tkinter import ttk           

root = tk.Tk()
root.title("Sympy")
root.geometry("655x350")
root. configure(bg="#6f8073")

style = ttk.Style()
style.configure("Cuestom.TFrame", background="#C8C6C9")

frame = ttk.Frame(root, padding="10 10 10 10", style="Cuestom.TFrame")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S,))

titulo = tk.Label(frame, text="Sympy", font=("Garamond", 24, "bold"), bg= "#C8C6C9", fg="black")
titulo.grid(column=0, row=0, sticky=tk.N, pady=(0, 10))

parrafo_texto= """Sympy permite hacer operaciones analíticas o con símbolos en lugar de con valores numéricos Al igual que en Python existen varios tipos de datos numéricos como enteros (int), decimales (float) o booleanos (bool:True, False, etc.), Sympy posee tres tipos de datos propios: Real, Rational e Integer, es decir, números reales, racionales y enteros. Estoquiere decir que Rational(1,2) representa 1/2, Rational(5,2) a 5/2, etc. en lugar de 0.5 o 2.5.

También existen algunas constantes especiales, como el número e o π, si embargo éstos se tratan con símbolos y no tienen un valor númerico determinado. Eso quiere decir que no se puede obtener un valor numérico de una operación usando el pi de Sympy, como (1+pi), como lo haríamos con el de Numpy, que es numérico:

Como se ve, sin embargo, se puede usar el método evalf() para evaluar una expresión para tener un valor en punto flotante (float).
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
    webbrowser.open_new("https://research.iac.es/sieinvens/python-course/sympy.html")
enlace.bind("<Button-1>", abrir_url)

root.mainloop()