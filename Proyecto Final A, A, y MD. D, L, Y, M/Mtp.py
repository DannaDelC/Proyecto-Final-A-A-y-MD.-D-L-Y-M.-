import tkinter as tk          
from tkinter import ttk           

root = tk.Tk()
root.title("Matplotlib")
root.geometry("655x351")
root. configure(bg="#6f8073")

style = ttk.Style()
style.configure("Cuestom.TFrame", background="#C8C6C9")

frame = ttk.Frame(root, padding="10 10 10 10", style="Cuestom.TFrame")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S,))

titulo = tk.Label(frame, text="Matplotlib", font=("Garamond", 24, "bold"), bg= "#C8C6C9", fg="black")
titulo.grid(column=0, row=0, sticky=tk.N, pady=(0, 10))

parrafo_texto= """Matplotlib es una biblioteca de visualización de datos potente y muy popular en Python. En este tutorial, analizaremos cómo crear gráficos de líneas, gráficos de barras y gráficos de dispersión en Matplotlib utilizando datos del mercado de valores en 2022. Estos son los gráficos básicos que le permitirán comenzar a comprender, visualizar y contar historias sobre los datos. La visualización de datos es una habilidad esencial para todos los analistas de datos y Matplotlib es una de las bibliotecas más populares para crear visualizaciones. 

Este tutorial requiere algunos conocimientos previos básicos sobre matrices NumPy y marcos de datos de Pandas. Cuando usemos esas bibliotecas, explicaremos rápidamente lo que estamos haciendo. El enfoque principal de este tutorial es Matplotlib, que funciona sobre estas estructuras de datos para crear visualizaciones. 
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
    webbrowser.open_new("https://www.datacamp.com/tutorial/matplotlib-tutorial-python")
enlace.bind("<Button-1>", abrir_url)

root.mainloop()