import tkinter as tk          
from tkinter import ttk           

root = tk.Tk()
root.title("Permutaciones")
root.geometry("655x351")
root. configure(bg="#6f8073")

style = ttk.Style()
style.configure("Cuestom.TFrame", background="#C8C6C9")

frame = ttk.Frame(root, padding="10 10 10 10", style="Cuestom.TFrame")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S,))

titulo = tk.Label(frame, text="Permutaciones", font=("Garamond", 24, "bold"), bg= "#C8C6C9", fg="black")
titulo.grid(column=0, row=0, sticky=tk.N, pady=(0, 10))

parrafo_texto= """Las permutaciones son diferentes formas de ordenar objetos en un orden determinado. También se pueden expresar como la reorganización de elementos en un orden lineal de un conjunto ya ordenado. El símbolo nortePAGa se utiliza para indicar el número de permutaciones de n objetos distintos, tomados de r en r. Bloquea horarios de autobuses, trenes o vuelos, asignación de códigos postales y números de teléfono. Estas son algunas situaciones en las que se utilizan permutaciones. Permutar significa posicionar. Aprendamos más sobre las permutaciones junto con algunos ejemplos resueltos.

Una permutación es una disposición ordenada de resultados y una combinación ordenada. Por ejemplo, hay 5 sillas y se van a sentar 3 personas. Tenemos 5 formas de sentar a la primera persona; 4 formas de sentar a la siguiente persona y 3 formas de sentar a la tercera persona. Por lo tanto, para encontrar la cantidad de formas de organizar 3 personas en 5 sillas, multiplicamos las opciones disponibles. Lo hacemos de 5 × 4 × 3 formas. Es decir, se puede hacer de 60 formas. Observe que 5 × 4 × 3 se puede escribir como (5!) / (2!) (o) (5!) / (5 - 3)!. Generalizando esto, obtenemos n opciones para llenar la primera silla, n-1 opciones para llenar la segunda y n-2 opciones para llenar la tercera silla. Por lo tanto, el número total de permutaciones (disposiciones) de r personas en n sillas se puede expresar como: n P r = n! / (n - r)!.
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
    webbrowser.open_new("https://www.cuemath.com/data/permutations/")
enlace.bind("<Button-1>", abrir_url)

root.mainloop()