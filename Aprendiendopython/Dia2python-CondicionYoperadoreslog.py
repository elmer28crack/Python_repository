

# -----------------------------
# 1. Estructura básica del if
# -----------------------------
edad = 18

print("1. Ejemplo básico de if:")
if edad >= 18:
    print("Eres mayor de edad.")
print("Fin del ejemplo\n")

# -----------------------------
# 2. If - Else
# -----------------------------
print("2. Ejemplo de if - else:")
if edad < 18:
    print("Eres menor de edad.")
else:
    print("Eres mayor de edad.")
print("Fin del ejemplo\n")

# -----------------------------
# 3. If - Elif - Else
# -----------------------------
nota = 85

print("3. Ejemplo de if - elif - else:")
if nota >= 90:
    print("Excelente")
elif nota >= 80:
    print("Muy bien")
elif nota >= 70:
    print("Aprobado")
else:
    print("Reprobado")
print("Fin del ejemplo\n")

# -----------------------------
# 4. Operadores de comparación
# -----------------------------
# ==  → igual que
# !=  → diferente de
# >   → mayor que
# <   → menor que
# >=  → mayor o igual que
# <=  → menor o igual que

x = 10
y = 5
print("4. Operadores de comparación:")
print("x == y:", x == y)
print("x != y:", x != y)
print("x > y:", x > y)
print("x < y:", x < y)
print("x >= y:", x >= y)
print("x <= y:", x <= y)
print("Fin del ejemplo\n")

# -----------------------------
# 5. Operadores lógicos
# -----------------------------
# and → devuelve True si ambas condiciones son verdaderas
# or  → devuelve True si al menos una condición es verdadera
# not → invierte el resultado (True → False, False → True)


edad = 20
tiene_permiso = True

print("5. Operadores lógicos:")
if edad >= 18 and tiene_permiso:
    print("Puedes conducir.")
else:
    print("No puedes conducir.")

if edad < 18 or not tiene_permiso:
    print("Requiere permiso o ser mayor de edad.")
else:
    print("Todo en orden.")
print("Fin del ejemplo\n")

# -----------------------------
# 6. Condiciones anidadas
# -----------------------------
print("6. If dentro de otro if:")
usuario = "Elmer"
contraseña = "1234"

if usuario == "Elmer":
    if contraseña == "1234":
        print("Acceso concedido.")
    else:
        print("Contraseña incorrecta.")
else:
    print("Usuario no encontrado.")
print("Fin del ejemplo\n")

# -----------------------------
# 7. Operador ternario (forma corta de if/else)
# -----------------------------
print("7. Operador ternario:")
edad = 16
mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"
print("Resultado:", mensaje)
print("Fin del ejemplo\n")

# -----------------------------
# 8. Uso combinado de comparadores y lógicos
# -----------------------------
print("8. Ejemplo combinado:")
a = 15
b = 10
c = 20

if (a > b and a < c) or (b == 10 and not c < 0):
    print("La condición combinada es VERDADERA.")
else:
    print("La condición combinada es FALSA.")
print("Fin del ejemplo\n")

# -----------------------------
# 9. Comparaciones múltiples en una sola línea
# -----------------------------
print("9. Comparaciones encadenadas:")
numero = 15
if 10 < numero < 20:
    print("El número está entre 10 y 20.")
else:
    print("El número no está en el rango.")
print("Fin del ejemplo\n")
