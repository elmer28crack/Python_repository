# -----------------------------
# 1. Ciclo for básico
# -----------------------------
print("1. Ciclo for básico:")
for i in range(5):  # range(5) genera los números 0, 1, 2, 3, 4
    print("Iteración:", i)
print("Fin del ciclo\n")

# -----------------------------
# 2. for con listas
# -----------------------------
print("2. Recorrer lista con for:")
frutas = ["manzana", "pera", "uva", "mango"]
for fruta in frutas:
    print("Fruta:", fruta)
print("Fin del ciclo\n")

# -----------------------------
# 3. for con texto (string)
# -----------------------------
print("3. Recorrer texto con for:")
palabra = "Python"
for letra in palabra:
    print("Letra:", letra)
print("Fin del ciclo\n")

# -----------------------------
# 4. range() – generar secuencias de números
# -----------------------------
print("4. Ejemplo de range():")
for num in range(2, 10, 2):  # inicio=2, fin=10, paso=2
    print("Número:", num)
print("Fin del ciclo\n")

# -----------------------------
# 5. Ciclo while básico
# -----------------------------
print("5. Ciclo while básico:")
contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1  # Incrementa para evitar ciclo infinito
print("Fin del ciclo\n")

# -----------------------------
# 6. Uso de break (detiene el ciclo)
# -----------------------------
print("6. Uso de break:")
for i in range(10):
    if i == 5:
        print("Se detiene el ciclo en", i)
        break
    print("i =", i)
print("Fin del ciclo\n")

# -----------------------------
# 7. Uso de continue (salta a la siguiente iteración)
# -----------------------------
print("7. Uso de continue:")
for i in range(1, 6):
    if i == 3:
        print("Salta el número 3")
        continue
    print("Número:", i)
print("Fin del ciclo\n")

# -----------------------------
# 8. Bucle while con break y continue
# -----------------------------
print("8. While con break y continue:")
n = 0
while True:  # bucle infinito hasta que se use break
    n += 1
    if n == 3:
        print("Salta el número 3")
        continue
    if n == 6:
        print("Rompe el ciclo en 6")
        break
    print("Número:", n)
print("Fin del ciclo\n")

# -----------------------------
# 9. Ciclo for anidado
# -----------------------------
print("9. Ciclo for anidado:")
for x in range(3):
    for y in range(2):
        print(f"Par (x={x}, y={y})")
print("Fin del ciclo\n")

# -----------------------------
# 10. Uso de else con ciclos
# -----------------------------
# El bloque else se ejecuta cuando el ciclo termina normalmente (sin break)
print("10. Else en ciclos:")
for i in range(3):
    print("Iteración:", i)
else:
    print("El ciclo for terminó correctamente.")
print("Fin del ciclo\n")

# -----------------------------
# 11. while con condición de entrada
# -----------------------------
print("11. while con condición de entrada:")
num = int(input("Ingresa un número mayor a 0 para contar atrás: "))
while num > 0:
    print("Cuenta atrás:", num)
    num -= 1
print("¡Despegue!\n")

# -----------------------------
# 12. for con enumerate() – obtener índice y valor
# -----------------------------
print("12. Uso de enumerate():")
colores = ["Rojo", "Verde", "Azul"]
for indice, color in enumerate(colores):
    print(f"Índice: {indice} | Color: {color}")
print("Fin del ciclo\n")

# -----------------------------
# 13. for con range(len()) – recorrer usando índices
# -----------------------------
print("13. Uso de range(len()):")
for i in range(len(frutas)):
    print(f"Índice {i}: {frutas[i]}")
print("Fin del ciclo\n")

# -----------------------------
# 14. Bucle infinito controlado manualmente
# -----------------------------
print("14. Bucle infinito controlado:")
x = 1
while True:
    print("Número:", x)
    x += 1
    if x > 5:
        break
print("Fin del ciclo\n")