
# -----------------------------
# 1. Creación de Strings
# -----------------------------
# Los strings pueden definirse con comillas simples o dobles.
texto1 = 'Hola Mundo'
texto2 = "Hola Python"
print(texto1)
print(texto2)

# -----------------------------
# 2. Strings multilínea
# -----------------------------
# Se usan tres comillas para escribir texto en varias líneas.
parrafo = """Este es un texto
que ocupa varias
líneas."""
print("\nTexto multilínea:")
print(parrafo)

# -----------------------------
# 3. Acceder a caracteres
# -----------------------------
# Los índices comienzan en 0
nombre = "Elmer"
print("\nAcceso por índice:")
print("Primer carácter:", nombre[0])
print("Último carácter:", nombre[-1])

# -----------------------------
# 4. Slicing (rebanado)
# -----------------------------
print("\nRebanado:")
print("Primeros tres:", nombre[:3])
print("Desde el segundo:", nombre[1:])
print("Rango 1 a 3:", nombre[1:4])

# -----------------------------
# 5. Longitud de un string
# -----------------------------
print("\nLongitud del nombre:", len(nombre))

# -----------------------------
# 6. Concatenación y repetición
# -----------------------------
saludo = "Hola "
persona = "Elmer"
print("\nConcatenación:", saludo + persona)
print("Repetición:", "Hola! " * 3)

# -----------------------------
# 7. Verificación de contenido
# -----------------------------
frase = "Aprender Python es divertido"
print("\nVerificación:")
print("'Python' está en frase:", "Python" in frase)
print("'Java' no está en frase:", "Java" not in frase)

# -----------------------------
# 8. Métodos comunes de strings
# -----------------------------
texto = "  python es genial  "
print("\nMétodos comunes:")
print("Mayúsculas:", texto.upper())
print("Minúsculas:", texto.lower())
print("Primera en mayúscula:", texto.capitalize())
print("Cada palabra en mayúscula:", texto.title())
print("Quitar espacios:", texto.strip())
print("Reemplazar texto:", texto.replace("python", "JavaScript"))

# -----------------------------
# 9. División y unión
# -----------------------------
oracion = "Aprender es divertido"
palabras = oracion.split()  # Divide en lista por espacios
print("\nSplit:", palabras)
unido = "-".join(palabras)  # Une la lista con guiones
print("Join:", unido)

# -----------------------------
# 10. Formateo de strings
# -----------------------------
nombre = "Elmer"
edad = 19

# Forma 1: concatenación
print("\nFormateo de texto:")
print("Hola, mi nombre es " + nombre + " y tengo " + str(edad) + " años.")

# Forma 2: format()
print("Hola, mi nombre es {} y tengo {} años.".format(nombre, edad))

# Forma 3: f-string (más moderna)
print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")

# -----------------------------
# 11. Escape de caracteres
# -----------------------------
frase_escape = "Ella dijo: \"Hola mundo\""
print("\nEscape de comillas:", frase_escape)
salto_linea = "Primera línea\nSegunda línea"
print("Con salto de línea:\n", salto_linea)
tabulacion = "Python\tes\tpoderoso"
print("Con tabulación:", tabulacion)

# -----------------------------
# 12. Substrings y comparación
# -----------------------------
texto_a = "python"
texto_b = "Python"
print("\nComparación:")
print("¿Son iguales?", texto_a == texto_b)
print("¿Son iguales (ignorando mayúsculas)?", texto_a.lower() == texto_b.lower())

# -----------------------------
# 13. Revertir string
# -----------------------------
palabra = "Python"
invertido = palabra[::-1]
print("\nRevertido:", invertido)

# -----------------------------
# 14. Contar y buscar
# -----------------------------
frase2 = "Me gusta programar en Python porque Python es divertido"
print("\nContar y buscar:")
print("Veces que aparece 'Python':", frase2.count("Python"))
print("Posición de 'programar':", frase2.find("programar"))
print("Posición de 'Java' (si no existe devuelve -1):", frase2.find("Java"))
