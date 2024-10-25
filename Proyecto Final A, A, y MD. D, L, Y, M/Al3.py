import tkinter as tk          
from tkinter import ttk           

root = tk.Tk()
root.title("Matriz por Gauss-Jordan")
root.geometry("655x351")
root. configure(bg="#6f8073") 

style = ttk.Style()
style.configure("Cuestom.TFrame", background="#C8C6C9")

frame = ttk.Frame(root, padding="10 10 10 10", style="Cuestom.TFrame")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S,))

titulo = tk.Label(frame, text="Matriz por Gauss-Jordan", font=("Garamond", 24, "bold"), bg= "#C8C6C9", fg="black")
titulo.grid(column=0, row=0, sticky=tk.N, pady=(0, 10))

parrafo_texto= """
Carl Friedrich Gauss vivió a finales del siglo XVIII y principios del XIX, pero se lo sigue considerando uno de los matemáticos más prolíficos de la historia. Sus aportes a la ciencia de las matemáticas y la física abarcan campos como el álgebra, la teoría de números, el análisis, la geometría diferencial, la astronomía y la óptica, entre otros. Sus descubrimientos sobre la teoría de las matrices cambiaron la forma de trabajar de los matemáticos durante los dos siglos pasados.

La primera vez que estudiamos la eliminación de Gauss-Jordan fue en la sección Sistemas de ecuaciones lineales: dos variables En esta sección volveremos a examinar esta técnica de resolver sistemas, esta vez mediante matrices.
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
    webbrowser.open_new("https://openstax.org/books/prec%C3%A1lculo-2ed/pages/9-6-resolver-sistemas-con-eliminacion-de-gauss-jordan")

enlace.bind("<Button-1>", abrir_url)

root.mainloop()



