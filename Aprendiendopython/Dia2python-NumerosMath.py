

# -----------------------------
# 1. Tipos de números
# -----------------------------
entero = 10            # int → número entero
decimal = 3.14         # float → número con decimales
complejo = 2 + 3j      # complex → número complejo (a + bj)

print("1. Tipos de números:")
print("Entero:", entero, "| Tipo:", type(entero))
print("Decimal:", decimal, "| Tipo:", type(decimal))
print("Complejo:", complejo, "| Tipo:", type(complejo))

# -----------------------------
# 2. Operaciones básicas
# -----------------------------
a = 10
b = 3
print("\n2. Operaciones básicas:")
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)
print("División entera:", a // b)  # devuelve solo la parte entera
print("Módulo (resto):", a % b)
print("Potencia:", a ** b)

# -----------------------------
# 3. Prioridad de operaciones
# -----------------------------
resultado = (a + b) * 2
print("\n3. Prioridad de operaciones:")
print("Resultado de (a + b) * 2 =", resultado)

# -----------------------------
# 4. Conversión de tipos
# -----------------------------
x = "15"
y = "3.5"
print("\n4. Conversión de tipos:")
print("De str a int:", int(x))
print("De str a float:", float(y))
print("De int a float:", float(entero))
print("De float a int:", int(decimal))

# -----------------------------
# 5. Redondeo y valor absoluto
# -----------------------------
num = -7.89
print("\n5. Redondeo y valor absoluto:")
print("round(7.89) =", round(7.89))
print("round(7.8912, 2) =", round(7.8912, 2))  # redondea a 2 decimales
print("abs(-7.89) =", abs(num))                # valor absoluto

# -----------------------------
# 6. Funciones matemáticas del módulo math
# -----------------------------
import math
print("\n6. Funciones del módulo math:")
print("Raíz cuadrada (sqrt):", math.sqrt(16))
print("Potencia (pow):", math.pow(2, 5))
print("Número pi:", math.pi)
print("Número e:", math.e)
print("Redondeo hacia abajo (floor):", math.floor(3.99))
print("Redondeo hacia arriba (ceil):", math.ceil(3.01))
print("Valor absoluto (fabs):", math.fabs(-15))
print("Logaritmo base 10:", math.log10(100))
print("Seno(90°):", math.sin(math.radians(90)))
print("Coseno(0°):", math.cos(math.radians(0)))

# -----------------------------
# 7. Números aleatorios (random)
# -----------------------------
import random
print("\n7. Números aleatorios:")
print("Número aleatorio entre 1 y 10:", random.randint(1, 10))
print("Número flotante aleatorio entre 0 y 1:", random.random())
print("Número aleatorio dentro de rango (0,100,5):", random.randrange(0, 100, 5))
print("Elegir elemento aleatorio de una lista:", random.choice([10, 20, 30, 40]))

# -----------------------------
# 8. Notación científica
# -----------------------------
num_cientifico = 1.2e3  # equivale a 1.2 × 10³ = 1200
print("\n8. Notación científica:")
print("1.2e3 =", num_cientifico)

# -----------------------------
# 9. Números complejos
# -----------------------------
c = 4 + 5j
print("\n9. Números complejos:")
print("Número complejo:", c)
print("Parte real:", c.real)
print("Parte imaginaria:", c.imag)
print("Conjugado:", c.conjugate())

# -----------------------------
# 10. Comparaciones y operadores lógicos
# -----------------------------
x = 8
y = 5
print("\n10. Comparaciones:")
print("x > y:", x > y)
print("x < y:", x < y)
print("x == y:", x == y)
print("x != y:", x != y)

# -----------------------------
# 11. Incrementos y asignaciones combinadas
# -----------------------------
z = 10
z += 5   # equivale a z = z + 5
print("\n11. Incremento combinado (+):", z)
z *= 2   # equivale a z = z * 2
print("Multiplicación combinada (*):", z)

# -----------------------------
# 12. Funciones útiles extra
# -----------------------------
numeros = [3, 7, 2, 9, 5]
print("\n12. Funciones extra:")
print("Máximo:", max(numeros))
print("Mínimo:", min(numeros))
print("Suma:", sum(numeros))
print("Promedio:", sum(numeros) / len(numeros))
