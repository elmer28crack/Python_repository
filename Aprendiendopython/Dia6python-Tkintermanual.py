"""
==============================
📘 MANUAL BÁSICO DE TKINTER
==============================

Entonces Tkinter funciona creando una ventana principal donde se agregan
componentes (widgets), los cuales responden a eventos del usuario,
por lo que la aplicación se vuelve interactiva, a diferencia de un
programa de consola lineal.

==============================
🖥️ 1. VENTANA PRINCIPAL
==============================
"""

import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Manual Tkinter")
ventana.geometry("400x400")

"""
Entonces la ventana principal es el contenedor de toda la interfaz,
por lo que todos los elementos deben colocarse dentro de ella,
a diferencia de un script normal que no tiene interfaz visual.
"""

# ==========================================
# 🧱 2. LABEL (TEXTO)
# ==========================================

label = tk.Label(ventana, text="Esto es un Label")
label.pack()

"""
Entonces el Label muestra texto en pantalla, por lo que se usa
para informar al usuario, a diferencia de print() que solo usa consola.
"""

# ==========================================
# ⌨️ 3. ENTRY (INPUT)
# ==========================================

entrada = tk.Entry(ventana)
entrada.pack()

"""
Entonces Entry permite al usuario escribir datos, y se obtiene con .get(),
por lo que el flujo depende del usuario, a diferencia de input().
"""

# ==========================================
# 🔘 4. BOTÓN
# ==========================================

def mostrar_texto():
    texto = entrada.get()
    print(texto)

boton = tk.Button(ventana, text="Mostrar texto", command=mostrar_texto)
boton.pack()

"""
Entonces el botón ejecuta una función cuando se hace clic,
por lo que conecta la interfaz con la lógica del programa,
a diferencia de ejecutar funciones directamente.
"""

# ==========================================
# 🔔 5. MESSAGEBOX (VENTANAS EMERGENTES)
# ==========================================

def alerta():
    messagebox.showinfo("Info", "Esto es una alerta")

boton_alerta = tk.Button(ventana, text="Mostrar alerta", command=alerta)
boton_alerta.pack()

"""
Entonces messagebox muestra mensajes emergentes,
por lo que mejora la interacción con el usuario,
a diferencia de solo imprimir texto.
"""

# ==========================================
# 📐 6. LAYOUTS
# ==========================================

# PACK (automático)
# widget.pack()

# GRID (filas y columnas)
# widget.grid(row=0, column=0)

# PLACE (posición exacta)
# widget.place(x=50, y=50)

"""
Entonces los layouts controlan la posición de los elementos,
por lo que definen la estructura visual,
a diferencia de solo crear widgets sin organizarlos.
"""

# ==========================================
# 🧼 7. MÉTODOS IMPORTANTES DE ENTRY
# ==========================================

def limpiar():
    entrada.delete(0, tk.END)

def insertar():
    entrada.insert(0, "Texto por defecto")

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
boton_limpiar.pack()

boton_insertar = tk.Button(ventana, text="Insertar texto", command=insertar)
boton_insertar.pack()

"""
Entonces puedes manipular el input dinámicamente,
por lo que puedes limpiar o modificar el contenido,
a diferencia de inputs estáticos.
"""

# ==========================================
# 🔁 8. VARIABLES TKINTER
# ==========================================

texto_var = tk.StringVar()

entrada_var = tk.Entry(ventana, textvariable=texto_var)
entrada_var.pack()

"""
Entonces las variables de Tkinter permiten sincronizar datos
con la interfaz automáticamente, por lo que los cambios se reflejan
sin actualizar manualmente, a diferencia de variables normales.
"""

# ==========================================
# 🚀 9. CAMBIAR TEXTO DINÁMICAMENTE
# ==========================================

def cambiar_label():
    label.config(text="Texto cambiado 😏")

boton_cambiar = tk.Button(ventana, text="Cambiar texto", command=cambiar_label)
boton_cambiar.pack()

"""
Entonces puedes modificar elementos en tiempo real,
por lo que la interfaz responde dinámicamente,
a diferencia de contenido fijo.
"""

# ==========================================
# 🔚 EJECUCIÓN
# ==========================================

ventana.mainloop()

"""
Entonces mainloop mantiene la aplicación corriendo,
por lo que espera eventos del usuario,
a diferencia de un programa que termina inmediatamente.

"""
"""
==============================
📘 MANUAL TKINTER - VENTANA
==============================

Entonces la ventana es el núcleo de toda la aplicación, por lo que controla
el tamaño, título, comportamiento y apariencia general, a diferencia de los
widgets que son solo elementos dentro de ella.

"""

import tkinter as tk

# ==========================================
# 🖥️ 1. CREAR VENTANA
# ==========================================

ventana = tk.Tk()

"""
Entonces Tk() crea la ventana principal de la aplicación,
por lo que todo lo demás depende de ella,
a diferencia de un programa sin interfaz.
"""

# ==========================================
# 🏷️ 2. TÍTULO DE LA VENTANA
# ==========================================

ventana.title("Mi Aplicación")

"""
Entonces .title() define el nombre que aparece arriba en la ventana,
por lo que ayuda a identificar la aplicación,
a diferencia de dejarla sin nombre.
"""

# ==========================================
# 📐 3. TAMAÑO DE LA VENTANA
# ==========================================

ventana.geometry("400x300")

"""
Entonces .geometry() define ancho x alto,
por lo que controlas el espacio visible,
a diferencia de usar tamaño automático.
"""

# ==========================================
# 📍 4. POSICIÓN EN PANTALLA
# ==========================================

ventana.geometry("400x300+100+100")

"""
Entonces puedes definir la posición (x, y),
por lo que decides dónde aparece la ventana,
a diferencia de dejarlo al sistema.
"""

# ==========================================
# 🚫 5. BLOQUEAR REDIMENSIONAMIENTO
# ==========================================

ventana.resizable(False, False)

"""
Entonces .resizable() controla si el usuario puede cambiar el tamaño,
por lo que puedes fijar el diseño,
a diferencia de permitir deformaciones.
"""

# ==========================================
# 📏 6. TAMAÑO MÍNIMO Y MÁXIMO
# ==========================================

ventana.minsize(300, 200)
ventana.maxsize(800, 600)

"""
Entonces defines límites de tamaño,
por lo que mantienes control sobre la interfaz,
a diferencia de dejarlo libre.
"""

# ==========================================
# 🎨 7. COLOR DE FONDO
# ==========================================

ventana.config(bg="lightblue")

"""
Entonces puedes cambiar el fondo,
por lo que mejoras el diseño visual,
a diferencia del gris por defecto.
"""

# ==========================================
# 🔝 8. SIEMPRE ENCIMA
# ==========================================

ventana.attributes("-topmost", True)

"""
Entonces la ventana se mantiene encima de todas,
por lo que no se pierde detrás de otras,
a diferencia del comportamiento normal.
"""

# ==========================================
# 🧊 9. TRANSPARENCIA
# ==========================================

ventana.attributes("-alpha", 0.9)

"""
Entonces puedes hacer la ventana semi-transparente,
por lo que puedes crear efectos visuales,
a diferencia de opacidad completa.
"""

# ==========================================
# ❌ 10. ICONO DE LA VENTANA
# ==========================================

# ventana.iconbitmap("icono.ico")

"""
Entonces puedes cambiar el icono de la ventana,
por lo que personalizas la app,
a diferencia del icono por defecto.
"""

# ==========================================
# 🔒 11. DESHABILITAR CIERRE
# ==========================================

def evitar_cierre():
    print("No puedes cerrar 😏")

ventana.protocol("WM_DELETE_WINDOW", evitar_cierre)

"""
Entonces controlas qué pasa cuando el usuario intenta cerrar,
por lo que puedes bloquear o manejar ese evento,
a diferencia del cierre automático.
"""

# ==========================================
# 🔁 12. OCULTAR Y MOSTRAR VENTANA
# ==========================================

# ventana.withdraw()  # Oculta
# ventana.deiconify() # Muestra

"""
Entonces puedes ocultar o mostrar la ventana,
por lo que puedes manejar múltiples pantallas,
a diferencia de una sola ventana fija.
"""

# ==========================================
# 🔄 13. ACTUALIZAR VENTANA
# ==========================================

# ventana.update()

"""
Entonces fuerzas la actualización de la interfaz,
por lo que reflejas cambios inmediatamente,
a diferencia de esperar eventos.
"""

# ==========================================
# ⏱️ 14. EJECUTAR FUNCIONES DESPUÉS DE TIEMPO
# ==========================================

def saludo():
    print("Hola después de 2 segundos")

ventana.after(2000, saludo)

"""
Entonces puedes ejecutar funciones con retraso,
por lo que creas temporizadores,
a diferencia de ejecución inmediata.
"""

# ==========================================
# 🔚 15. LOOP PRINCIPAL
# ==========================================

ventana.mainloop()

"""
Entonces mainloop mantiene la ventana activa,
por lo que espera interacción del usuario,
a diferencia de un script que termina.

"""
"""
==============================
📘 MANUAL TKINTER - LABEL
==============================

Entonces el Label es un widget que muestra texto o imágenes en la ventana,
por lo que se usa para informar o mostrar datos al usuario, a diferencia
de print() que solo funciona en consola.

"""

import tkinter as tk

ventana = tk.Tk()
ventana.title("Manual Label")
ventana.geometry("400x400")

# ==========================================
# 🧱 1. CREAR LABEL BÁSICO
# ==========================================

label = tk.Label(ventana, text="Hola mundo")
label.pack()

"""
Entonces el Label muestra texto en pantalla,
por lo que es un elemento visual informativo,
a diferencia de otros widgets interactivos.
"""

# ==========================================
# 🎨 2. COLOR DE TEXTO Y FONDO
# ==========================================

label_color = tk.Label(ventana, text="Colores", fg="white", bg="black")
label_color.pack()

"""
Entonces puedes cambiar colores,
por lo que mejoras la apariencia,
a diferencia del estilo por defecto.
"""

# ==========================================
# 🔤 3. FUENTE Y TAMAÑO
# ==========================================

label_fuente = tk.Label(ventana, text="Texto grande", font=("Arial", 16))
label_fuente.pack()

"""
Entonces puedes modificar la fuente,
por lo que controlas el estilo visual,
a diferencia del tamaño estándar.
"""

# ==========================================
# 📏 4. TAMAÑO (width, height)
# ==========================================

label_size = tk.Label(ventana, text="Tamaño fijo", width=20, height=2, bg="lightgray")
label_size.pack()

"""
Entonces defines el tamaño del label,
por lo que puedes controlar el espacio,
a diferencia de tamaño automático.
"""

# ==========================================
# 📍 5. ALINEACIÓN DEL TEXTO
# ==========================================

label_align = tk.Label(ventana, text="Alineado izquierda", anchor="w", width=20)
label_align.pack()

"""
Entonces anchor define la posición del texto dentro del label,
por lo que puedes alinearlo,
a diferencia del centrado por defecto.
"""

# ==========================================
# 🧭 6. POSICIONAMIENTO
# ==========================================

label_pack = tk.Label(ventana, text="pack()")
label_pack.pack()

label_grid = tk.Label(ventana, text="grid()")
label_grid.grid(row=0, column=1)

label_place = tk.Label(ventana, text="place()")
label_place.place(x=200, y=200)

"""
Entonces puedes usar pack, grid o place,
por lo que controlas la ubicación,
a diferencia de no posicionarlos.
"""

# ==========================================
# 🔄 7. CAMBIAR TEXTO DINÁMICAMENTE
# ==========================================

def cambiar_texto():
    label.config(text="Texto cambiado 😏")

boton = tk.Button(ventana, text="Cambiar Label", command=cambiar_texto)
boton.pack()

"""
Entonces puedes modificar el contenido en tiempo real,
por lo que la interfaz responde a eventos,
a diferencia de contenido fijo.
"""

# ==========================================
# 🔁 8. USO DE StringVar()
# ==========================================

texto_var = tk.StringVar()
texto_var.set("Texto inicial")

label_var = tk.Label(ventana, textvariable=texto_var)
label_var.pack()

def actualizar_var():
    texto_var.set("Nuevo texto dinámico")

boton_var = tk.Button(ventana, text="Actualizar con StringVar", command=actualizar_var)
boton_var.pack()

"""
Entonces StringVar conecta datos con el label,
por lo que se actualiza automáticamente,
a diferencia de usar config manual.
"""

# ==========================================
# 🖼️ 9. LABEL CON IMAGEN
# ==========================================

# NOTA: necesitas una imagen en tu carpeta
# imagen = tk.PhotoImage(file="imagen.png")
# label_img = tk.Label(ventana, image=imagen)
# label_img.pack()

"""
Entonces el Label también puede mostrar imágenes,
por lo que sirve como elemento visual,
a diferencia de solo texto.
"""

# ==========================================
# ✂️ 10. MULTILÍNEA Y AJUSTE
# ==========================================

label_multilinea = tk.Label(
    ventana,
    text="Este es un texto largo que se ajusta automáticamente",
    wraplength=150,
    justify="left"
)
label_multilinea.pack()

"""
Entonces puedes manejar texto largo,
por lo que se adapta al espacio,
a diferencia de cortarse.
"""

# ==========================================
# 🔲 11. BORDES Y RELIEVE
# ==========================================

label_borde = tk.Label(ventana, text="Con borde", bd=2, relief="solid")
label_borde.pack()

"""
Entonces puedes agregar bordes,
por lo que destacas elementos,
a diferencia de un label plano.
"""

# ==========================================
# 🔚 EJECUCIÓN
# ==========================================

ventana.mainloop()

"""
Entonces mainloop mantiene la interfaz activa,
por lo que el usuario puede interactuar,
a diferencia de un programa que termina.

==============================
✅ FIN DEL MANUAL
==============================
"""