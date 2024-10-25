import tkinter as tk
import subprocess

def run_AL():
    subprocess.run(['python', 'AL.py'])

def run_MD():
    subprocess.run(['python', 'MD.py'])

def run_Al1():
    subprocess.run(['python', 'Al1.py'])

def run_Al2():
    subprocess.run(['python', 'Al2.py'])

def run_Al3():
    subprocess.run(['python', 'Al3.py'])

def run_Al4(): 
    subprocess.run(['python', 'Al4.py'])

def run_Md1():
    subprocess.run(['python', 'Md1.py'])

def run_Md2():
    subprocess.run(['python', 'Md2.py'])

def run_Tk ():
    subprocess.run(['python', 'Tk.py'])

def run_Np():
    subprocess.run(['python', 'Np.py'])

def run_Sp():
    subprocess.run(['python', 'Sp.py'])

def run_Mtp():
    subprocess.run(['python', 'Mtp.py'])

def run_Scp():
    subprocess.run(['python', 'Scp.py'])

def run_Pil():
    subprocess.run(['python', 'Pil.py'])


def show_algebra():
    algebra_window = tk.Toplevel(root)
    algebra_window.title("Álgebra Lineal")
    algebra_window.configure(bg="#EADEE2")
    tk.Label(algebra_window, text="Álgebra Lineal", font=("Garamond", 30, "bold"), bg= "#EADEE2", fg="#6E7E71").pack(pady=20) 
    tk.Button(algebra_window, text="Definición de matrices", font=("Garamond", 20, "bold"),bg= "#EADEE2", fg="#6E7E71", anchor='w', command=run_Al1).pack(fill='both', pady=20)
    tk.Button(algebra_window, text="Matriz inversa", font=("Garamond", 20, "bold"), bg= "#EADEE2", fg="#6E7E71", anchor='w', command=run_Al2).pack(fill='both', pady=20)
    tk.Button(algebra_window, text="Matriz por Gauss-Jordan", font=("Garamond", 20, "bold"), bg= "#EADEE2", fg="#6E7E71", anchor='w', command=run_Al3).pack(fill='both', pady=20)
    tk.Button(algebra_window, text="Matriz por regla de Cramer", font=("Garamond", 20, "bold"), bg= "#EADEE2", fg="#6E7E71", anchor='w', command=run_Al4).pack(fill='both',pady=20)
    tk.Button(algebra_window, text="Calculadora de matrices", font=("Arial", 12, "bold"), bg="#a9a5a2", fg="#ffffff", command=run_AL).pack(pady=20)

       

def show_discrete_math():
    discrete_window = tk.Toplevel(root)
    discrete_window.title("Matemáticas Discreta")
    discrete_window.configure(bg='#EADEE2')
    tk.Label(discrete_window, text="Matemática Discreta", font=("Garamond", 30, "bold"),bg= "#EADEE2", fg="#6E7E71").pack(pady=20)
    tk.Button(discrete_window, text="Permutaciones", font=("Arial", 12), bg= "#EADEE2", fg="#6E7E71", anchor='n', command=run_Md1).pack(fill='both', pady=5)
    tk.Button(discrete_window, text="Combinaciones", font=("Arial", 12),bg= "#EADEE2", fg="#6E7E71", anchor='n', command=run_Md2).pack(fill='both', pady=5)
    tk.Button(discrete_window, text="Calculadora de permutaciones y combinaciones", font=("Arial", 12, "bold"), bg='#a9a5a2', fg="#ffffff", command=run_MD).pack(pady=20)


def show_algorithms():
    algorithms_window = tk.Toplevel(root)
    algorithms_window.title("Algoritmo")
    algorithms_window.configure(bg="#EADEE2")
    tk.Label(algorithms_window, text="Librerías en Python", font=("Garamond", 20, "bold"), bg= "#EADEE2", fg="#6E7E71").pack(pady=10)

    tk.Button(algorithms_window, text="Tkinter", font=("Arial", 15), bg= "#EADEE2", fg="#6E7E71", anchor='n', command=run_Tk).pack(fill="both", pady=5)
    tk.Button(algorithms_window, text="Numpy", font=("Arial", 15), bg= "#EADEE2", fg="#6E7E71", anchor='n', command=run_Np).pack(fill="both", pady=5)
    tk.Button(algorithms_window, text="Sympy", font=("Arial", 15), bg= "#EADEE2", fg="#6E7E71", anchor='n', command=run_Sp).pack(fill='both', pady=5)
    tk.Button(algorithms_window, text="Matplotlib", font=("Arial", 15), bg= "#EADEE2", fg="#6E7E71", anchor='n', command=run_Mtp).pack(fill='both', pady=5)
    tk.Button(algorithms_window, text="Scipy", font=("Arial", 15), bg= "#EADEE2", fg="#6E7E71", anchor='n', command=run_Scp).pack(fill='both', pady=5)
    tk.Button(algorithms_window, text="Pillow", font=("Arial", 15), bg= "#EADEE2", fg="#6E7E71", anchor='n', command=run_Pil).pack(fill="both", pady=5)
    

def show_credits():
    credits_window = tk.Toplevel(root)
    credits_window.title("Créditos")
    credits_window.configure(bg="#c8c6c9")
    tk.Label(credits_window, text="Integrantes del Proyecto", font=("Garamond", 30, "bold"), bg="#c8c6c9", fg="#000000").pack(pady=20)
    tk.Label(credits_window, text="1. Danna Lucrecia Del Cid López", font=("Georgia", 20), bg="#c8c6c9", fg="#000000", anchor='w').pack(fill='both', pady=5)
    tk.Label(credits_window, text="2. Marlyn Yaneth Ixcoy García", font=("Georgia", 20), bg="#c8c6c9", fg="#000000", anchor='w').pack(fill='both', pady=5)
    tk.Label(credits_window, text="3. Mercedes María José Vásquez Méndez", font=("Georgia", 20),bg="#c8c6c9", fg="#000000",anchor='w').pack(fill='both', pady=5)
    tk.Label(credits_window, text="4. Luis Enrique Portillo", font=("Georgia", 20),bg="#c8c6c9", fg="#000000",anchor='w').pack(fill='both', pady=5)
    
root = tk.Tk()
root.title("Menú Principal")
 
frame = tk.Frame(root, bg="#f3eaf4")
frame.pack(pady=20, padx=20)

tk.Label(frame, text="Bienvenidos a nuestro Proyecto", font=("Rockwell", 35, "bold"), bg="#f3eaf4").pack(pady=20)

tk.Button(frame, text="Álgebra Lineal", font=("Arial", 20, "bold"), bg="#bca3ac", command=show_algebra).pack(pady=5)
tk.Button(frame, text="Mate Discreta", font=("Arial", 20, "bold"), bg="#bca3ac", command=show_discrete_math).pack(pady=5)
tk.Button(frame, text="Algoritmos", font=("Arial", 20, "bold"), bg="#bca3ac", command=show_algorithms).pack(pady=5)
tk.Button(frame, text="Créditos", font=("Arial", 20, "bold"), bg="#bca3ac", command=show_credits).pack(pady=5)

root.mainloop()