
texto = "  Python es genial y divertido  "

# -----------------------------
# 1. upper() – convierte a mayúsculas
# -----------------------------
print("1. upper() →", texto.upper())

# -----------------------------
# 2. lower() – convierte a minúsculas
# -----------------------------
print("2. lower() →", texto.lower())

# -----------------------------
# 3. capitalize() – pone la primera letra en mayúscula
# -----------------------------
print("3. capitalize() →", texto.capitalize())

# -----------------------------
# 4. title() – convierte la primera letra de cada palabra en mayúscula
# -----------------------------
print("4. title() →", texto.title())

# -----------------------------
# 5. strip() – elimina espacios en blanco al inicio y al final
# -----------------------------
print("5. strip() →", texto.strip())

# -----------------------------
# 6. lstrip() y rstrip() – eliminan espacios a la izquierda o derecha
# -----------------------------
print("6. lstrip() →", texto.lstrip())
print("   rstrip() →", texto.rstrip())

# -----------------------------
# 7. replace() – reemplaza partes del texto
# -----------------------------
print("7. replace('Python', 'Java') →", texto.replace("Python", "Java"))

# -----------------------------
# 8. split() – divide el texto en una lista
# -----------------------------
print("8. split() →", texto.split())

# -----------------------------
# 9. join() – une una lista en un string
# -----------------------------
palabras = ["Python", "es", "genial"]
print("9. join() →", "-".join(palabras))

# -----------------------------
# 10. find() – devuelve la posición de una palabra (o -1 si no existe)
# -----------------------------
print("10. find('genial') →", texto.find("genial"))
print("   find('Java') →", texto.find("Java"))

# -----------------------------
# 11. count() – cuenta cuántas veces aparece una palabra
# -----------------------------
print("11. count('es') →", texto.count("es"))

# -----------------------------
# 12. startswith() – verifica si el texto empieza con algo
# -----------------------------
print("12. startswith('Python') →", texto.strip().startswith("Python"))

# -----------------------------
# 13. endswith() – verifica si el texto termina con algo
# -----------------------------
print("13. endswith('divertido') →", texto.strip().endswith("divertido"))

# -----------------------------
# 14. isalpha() – True si solo hay letras (sin espacios ni números)
# -----------------------------
solo_letras = "PythonEsGenial"
print("14. isalpha() →", solo_letras.isalpha())

# -----------------------------
# 15. isdigit() – True si solo hay números
# -----------------------------
solo_numeros = "12345"
print("15. isdigit() →", solo_numeros.isdigit())

# -----------------------------
# 16. isalnum() – True si solo hay letras y/o números (sin espacios)
# -----------------------------
mixto = "Python123"
print("16. isalnum() →", mixto.isalnum())

# -----------------------------
# 17. isspace() – True si solo hay espacios
# -----------------------------
solo_espacios = "   "
print("17. isspace() →", solo_espacios.isspace())

# -----------------------------
# 18. swapcase() – invierte mayúsculas y minúsculas
# -----------------------------
ejemplo = "PyThOn"
print("18. swapcase() →", ejemplo.swapcase())

# -----------------------------
# 19. zfill() – agrega ceros a la izquierda hasta alcanzar el largo indicado
# -----------------------------
numero = "42"
print("19. zfill(5) →", numero.zfill(5))  # Resultado: "00042"

# -----------------------------
# 20. center(), ljust(), rjust() – alinean texto
# -----------------------------
palabra = "Hola"
print("20. center(10, '-') →", palabra.center(10, '-'))
print("    ljust(10, '-') →", palabra.ljust(10, '-'))
print("    rjust(10, '-') →", palabra.rjust(10, '-'))

# -----------------------------
# 21. casefold() – igual que lower(), pero más fuerte (para idiomas con acentos)
# -----------------------------
texto2 = "PYTHON ES GENIAL"
print("21. casefold() →", texto2.casefold())

# -----------------------------
# 22. encode() y decode() – convierten texto a bytes y viceversa
# -----------------------------
print("22. encode() →", texto.encode("utf-8"))
print("    decode() →", texto.encode("utf-8").decode("utf-8"))
