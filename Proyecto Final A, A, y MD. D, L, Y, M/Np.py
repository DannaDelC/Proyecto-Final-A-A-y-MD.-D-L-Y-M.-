import tkinter as tk          
from tkinter import ttk           

root = tk.Tk()
root.title("Numpy")
root.geometry("655x351")
root. configure(bg="#6f8073")

style = ttk.Style()
style.configure("Cuestom.TFrame", background="#C8C6C9")

frame = ttk.Frame(root, padding="10 10 10 10", style="Cuestom.TFrame")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S,))

titulo = tk.Label(frame, text="Numpy", font=("Garamond", 24, "bold"), bg= "#C8C6C9", fg="black")
titulo.grid(column=0, row=0, sticky=tk.N, pady=(0, 10))

parrafo_texto= """NumPy (se pronuncia "numb pie") es uno de los paquetes más importantes a entender cuando estás comenzando a aprender Python.

El paquete es conocido por una estructura de datos muy útil llamado arreglo de NumPy. NumPy también permite a los desarrolladores de Python realizar en forma rápida una amplia variedad de cálculo numéricos.

Este tutorial te enseñará los fundamentos de NumPy que puedes usar para crear aplicaciones numéricas en Python

NumPy es una librería de Python para computación científica. NumPy significa  Python numérico. Aquí está la descripción oficial de la librería indicada en su página web: "NumPy es el paquete fundamental para la computación científica con Python. Contiene entre otras cosas:
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
    webbrowser.open_new("https://www.freecodecamp.org/espanol/news/la-guia-definitiva-del-paquete-numpy-para-computacion-cientifica-en-python/")
enlace.bind("<Button-1>", abrir_url)

root.mainloop()