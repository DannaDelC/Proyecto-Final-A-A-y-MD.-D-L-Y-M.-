import tkinter as tk          
from tkinter import ttk           

root = tk.Tk()
root.title("Scipy")
root.geometry("655x350")
root. configure(bg="#6f8073")

style = ttk.Style()
style.configure("Cuestom.TFrame", background="#C8C6C9")

frame = ttk.Frame(root, padding="10 10 10 10", style="Cuestom.TFrame")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S,))

titulo = tk.Label(frame, text="Scipy", font=("Garamond", 24, "bold"), bg= "#C8C6C9", fg="black")
titulo.grid(column=0, row=0, sticky=tk.N, pady=(0, 10))

parrafo_texto= """SciPy es una colección de algoritmos matemáticos y funciones prácticas creadas sobre la extensión NumPy de Python. Añade una potencia significativa a la sesión interactiva de Python al proporcionar al usuario comandos y clases de alto nivel para manipular y visualizar datos. Con SciPy, una sesión interactiva de Python se convierte en un entorno de procesamiento de datos y creación de prototipos de sistemas que rivaliza con sistemas como MATLAB, IDL, Octave, R-Lab y SciLab.

El beneficio adicional de basar SciPy en Python es que también se obtiene un potente lenguaje de programación para desarrollar programas sofisticados y aplicaciones especializadas. Las aplicaciones científicas que utilizan SciPy se benefician del desarrollo de módulos adicionales en numerosos nichos del panorama del software por parte de desarrolladores de todo el mundo. Todo, desde programación paralela hasta subrutinas y clases para bases de datos y web, se ha puesto a disposición del programador Python. 
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
    webbrowser.open_new("https://docs.scipy.org/doc/scipy-1.8.1/tutorial/general.html")
enlace.bind("<Button-1>", abrir_url)

root.mainloop()

