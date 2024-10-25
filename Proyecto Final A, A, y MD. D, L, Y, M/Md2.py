import tkinter as tk          
from tkinter import ttk           

root = tk.Tk()
root.title("Combinaciones")
root.geometry("655x351")
root. configure(bg="#6f8073")

style = ttk.Style()
style.configure("Cuestom.TFrame", background="#C8C6C9")

frame = ttk.Frame(root, padding="10 10 10 10", style="Cuestom.TFrame")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S,))

titulo = tk.Label(frame, text="Combinaciones", font=("Garamond", 24, "bold"), bg= "#C8C6C9", fg="black")
titulo.grid(column=0, row=0, sticky=tk.N, pady=(0, 10))

parrafo_texto= """Se refiere a la selección de elementos sin considerar el orden. Es una forma de contar o enumerar conjuntos sin orden, que son conjuntos donde el orden de los elementos no importa. En matemáticas, las combinaciones se utilizan en el estudio de la probabilidad, la estadística y la combinatoria. Tienen varias propiedades importantes:

1. Argumentos Enteros No Negativos
2. Propiedad de Simetría
3. Propiedad de Adición
4. Propiedad Multiplicativa
5. Teorema Binomial
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
    webbrowser.open_new("https://www.ck12.org/flexi/es/grado-6/combinaciones/explica-las-propiedades-de-las-combinaciones/")
enlace.bind("<Button-1>", abrir_url)

root.mainloop()