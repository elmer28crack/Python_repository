


#---------------------------------calculadora basica-------------------------
# resultado = 0
# desicion2 = ""
# desicion = 0
# numero = int(input("Ingresa el primer numero: "))
# operacion = input("Ingresa la operacion (Las operaciones son: suma, resta, multiplicacion, division): ")

# while desicion == 0:
#     numero2 = int(input("Ingresa el segundo numero: "))   
#     if operacion == "suma":
#         resultado = numero+numero2
#         desicion+=1
#         break
#     elif operacion == "resta":
#         resultado= numero-numero2
#         break
#     elif operacion == "multiplicacion":
#         resultado= numero*numero2
#         break
#     elif operacion == "division":
#         resultado= numero/numero2
#         break
#     elif operacion != "suma" and operacion != "resta" and operacion != "multiplicacion" and operacion != "division":
#         print("Operacion no valida, intenta de nuevo")
#         operacion = input("Ingresa la operacion (Las operaciones son: suma, resta, multiplicacion, division): ")
#         continue
# print("Su resultado es ",resultado)
#--------------------------------------------------------------------------------


#----------numeros primos---------------
# numero = 0
# contador = 0
# for i in range(1, numero + 1, 1):
#     if numero % i == 0:
#         contador = contador + 1
# if contador > 2:
#     print(numero,"no es primo")
# else:
#     print(numero,"es primo")
#---------------------------------------


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