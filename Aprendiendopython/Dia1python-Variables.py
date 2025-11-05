# -----------------------------
# 1. Declaración de variables
# -----------------------------
# En Python, no se necesita declarar el tipo de la variable.
# Se asigna automáticamente según el valor.

nombre = "Elmer"        # tipo str (cadena de texto)
edad = 19               # tipo int (entero)
altura = 1.78           # tipo float (decimal)
es_estudiante = True    # tipo bool (booleano)
materias = ["Mate", "Física", "Programación"]  # tipo list (lista)
puntuaciones = (10, 8, 9)                       # tipo tuple (tupla)
datos = {"nombre": "Elmer", "edad": 19}         # tipo dict (diccionario)
conjunto = {"Python", "Java", "C++"}            # tipo set (conjunto)

# Mostrar los valores
print("Nombre:", nombre)
print("Edad:", edad)
print("Altura:", altura)
print("¿Es estudiante?", es_estudiante)
print("Materias:", materias)
print("Puntuaciones:", puntuaciones)
print("Datos:", datos)
print("Conjunto:", conjunto)

# -----------------------------
# 2. Saber el tipo de una variable
# -----------------------------
print("\nTipos de variables:")
print("nombre:", type(nombre))
print("edad:", type(edad))
print("altura:", type(altura))
print("es_estudiante:", type(es_estudiante))

# -----------------------------
# 3. Reasignación de variables
# -----------------------------
# Puedes cambiar el valor de una variable en cualquier momento.
edad = 20
nombre = "Elmer Ramírez"
print("\nNueva edad:", edad)
print("Nuevo nombre:", nombre)

# -----------------------------
# 4. Variables múltiples
# -----------------------------
# Se pueden asignar varios valores en una línea:
a, b, c = 5, 10, 15
print("\nValores múltiples:", a, b, c)

# O asignar el mismo valor a varias variables:
x = y = z = "Pythonista"
print("Mismo valor:", x, y, z)

# -----------------------------
# 5. Convención de nombres
# -----------------------------
# - Deben comenzar con letra o guion bajo (_)
# - No pueden comenzar con número
# - No se permiten espacios
# - Usar estilo snake_case

_variable_correcta = "válido"
VariableIncorrecta2 = "válido, pero no recomendado"
# 2variable = "inválido" ❌ (no se puede iniciar con número)

# -----------------------------
# 6. Conversión de tipos (Casting)
# -----------------------------
numero_str = "123"
numero_int = int(numero_str)
numero_float = float(numero_str)
print("\nConversiones:")
print("De str a int:", numero_int)
print("De str a float:", numero_float)

# -----------------------------
# 7. Variables dinámicas
# -----------------------------
# El tipo puede cambiar durante la ejecución:
valor = 10
print("\nValor inicial:", valor, type(valor))
valor = "Diez"
print("Valor cambiado:", valor, type(valor))

# -----------------------------
# 8. Constantes (por convención)
# -----------------------------
# Python no tiene constantes reales, pero se usa mayúsculas para indicarlas.
PI = 3.1416
GRAVEDAD = 9.8
print("\nConstantes:", PI, GRAVEDAD)

# -----------------------------
# 9. Desempaquetado
# -----------------------------
# Extraer valores de listas o tuplas en variables individuales
colores = ("Rojo", "Verde", "Azul")
r, g, b = colores
print("\nDesempaquetado:")
print("Rojo:", r)
print("Verde:", g)
print("Azul:", b)