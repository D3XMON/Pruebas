import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import sqlite3
import requests
from tkinter import PhotoImage
from PIL import Image, ImageTk
import threading

# --- DB Setup (Una sola vez)
conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT,
    contraseña TEXT
)
''')
cursor.execute("INSERT OR IGNORE INTO usuarios (usuario, contraseña) VALUES (?, ?)", ('admin', '1234'))
conn.commit()
conn.close()

# --- Función para cargar imagen desde URL
def cargar_imagen(url, size=(100, 100)):
    from io import BytesIO
    img_data = requests.get(url).content
    img = Image.open(BytesIO(img_data)).resize(size)
    return ImageTk.PhotoImage(img)

# --- Interfaz principal
root = ttk.Window(themename="vapor")
root.title("Login - Rick and Morty App")
root.geometry("500x600")

frame = ttk.Frame(root, padding=20)
frame.pack(expand=True)

# --- Título centrado y en negrita
titulo = ttk.Label(frame, text="Bienvenido.", font=("Segoe UI", 20, "bold"), anchor="center")
titulo.pack(pady=20)

# --- Entradas
usuario = ttk.Entry(frame, width=30, font=("Segoe UI", 12))
usuario.insert(0, "Usuario")
usuario.pack(pady=5)

clave = ttk.Entry(frame, width=30, font=("Segoe UI", 12), show="*")
clave.insert(0, "Contraseña")
clave.pack(pady=5)

# --- Imagen de carga
cargando_img = ImageTk.PhotoImage(Image.open("loader.gif").resize((80, 80)))
cargando_label = ttk.Label(frame, image=cargando_img)

# --- Mostrar Rick & Morty API
def mostrar_personajes():
    limpiar_pantalla()
    ttk.Label(frame, text="Personajes de Rick and Morty", font=("Segoe UI", 16, "bold")).pack(pady=10)

    r = requests.get("https://rickandmortyapi.com/api/character")
    data = r.json()
    for p in data["results"][:3]:
        img = cargar_imagen(p["image"])
        img_label = ttk.Label(frame, image=img)
        img_label.image = img
        img_label.pack(pady=5)
        ttk.Label(frame, text=f"{p['name']} ({p['status']})", font=("Segoe UI", 12, "bold")).pack()

# --- Limpiar pantalla
def limpiar_pantalla():
    for widget in frame.winfo_children():
        widget.destroy()

# --- Validar login
def login():
    cargando_label.pack(pady=20)
    root.after(2000, validar_login)

def validar_login():
    u = usuario.get()
    c = clave.get()
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios WHERE usuario = ? AND contraseña = ?', (u, c))
    resultado = cursor.fetchone()
    conn.close()
    cargando_label.pack_forget()

    if resultado:
        mostrar_personajes()
    else:
        ttk.Label(frame, text="❌ Usuario o contraseña incorrectos", foreground="red").pack(pady=10)

# --- Botón estilizado sin esquinas
estilo = ttk.Style()
estilo.configure("TButton", font=("Segoe UI", 12, "bold"), borderwidth=0, relief="flat")

btn = ttk.Button(frame, text="Entrar", command=login, bootstyle="info-outline")
btn.pack(pady=20)

root.mainloop()
