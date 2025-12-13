# # --------------sacando el doble-------------------
# # n1 = int(input("ingresa un numero ")) 
# # print("el doble es",n1*2)

# # ---------------sumando 2 numero------
# # n1 = int(input("ingresa el primer numero #1: "))
# # n2 = int(input("ingresa el segundo numero #2: "))
# # print("El resultado de la suma es: ", n1+n2)

# #---------limite por ususario-----------
# # n1 = int(input("Ingresa el limite ")) 
# # for i in range(1,n1+1,1): print(i)

# # ----------------posi, nega o cero-----
# # n1 = float(input("Ingresa el numero y te dire si es positivo, negativo o cero ")) 
# # if(n1 > 0): 
# #     print("El numero es positivo") 
# # elif(n1 < 0): 
# #     print("El numero es negativo") 
# # else: 
# #     print("El numero es cero")



# # ---------mayor o menor (edad)--------
# # n1 = int(input("Ingresa tu edad: ")) 
# # if(n1 >= 18): 
# #     print("eres mayor de edad") 
# # else: 
# #     print("eres menor de edad")



# #---------la tabla multi-----------
# # n1 = int(input("""ingresa un numero para
# # darte la tabla del 1 al 10 de ese numero """)) 
# # for i in range(1,10+1): 
# #     print(n1,"x",i,"=",n1*i)


# #----------agregar a una lista de 5-------
# # lista = [] 
# # for i in range(5): 
# #     n1 = int(input("Ingresa un numero: ")) 
# #     lista.append(n1) 
# # print(lista)


# # ------el mas grande de la lista (ni idea del max xd)-----
# # lista = [] 
# # respuesta = "" 
# # while respuesta != "fin": 
# #     respuesta = input("Ingresa un numero y fin para que se acabe esta vaina: ") 
# #     if respuesta.lower() == "fin": 
# #         break 
# #     lista.append(int(respuesta)) 
# #     lista.sort() 
# # print(f"El numero mas alto de todo lo que ingresaste es: {lista[lista.__len__()-1]}")


# #-------------------intento de conteo de palabras------------


# # pala = input("ingresa palabras ")
# # arra = pala.split(' ')
# # elnuevo = {}
# # vamoaver=False


# # for i in range(len(arra)):
# #     vamoaver=elnuevo.__contains__(arra[i])
# #     if vamoaver == False:
# #         elnuevo[arra[i]] = ''
# #     else:
# #         print("palabra existente")
# # print(elnuevo)


# #-------chatgpt metiendo mano en el conteo de palabras-------------

# # texto = input("Ingresa un texto: ")

# # palabras = texto.split()
# # obajetoalamcen = {}

# # for palabra in palabras:
# #     if palabra in obajetoalamcen:
# #         obajetoalamcen[palabra] += 1
# #     else:
# #         obajetoalamcen[palabra] = 1

# # for palabra, cantidad in obajetoalamcen.items():
# #     print(f"{palabra}: {cantidad}")


# # texto = input("ingresa palabras y te contare cuantas veces se repiten: ")
# # arratext= texto.split(' ')
# # var = 0
# # var2 = []
# # for i in range(len(arratext)):
# #     print(arratext[i])
# #     for j in range(len(arratext)):
# #         print(arratext[j])
# #         if arratext[j] == arratext[i]:
# #             print("se repitio",arratext[j], arratext[i])
# #             var+=1
# #     var2.append(var)
# # print(var)
# # print(var2)

# dna_sequence = ['GCT', 'AGC', 'AGG', 'TAA', 'ACT', 'CAT', 'TAT', 'CCC', 'ACG', 'GAA', 'ACC', 'GGA']
# item_to_find = 'GCT'
# item_found = False

# for i in dna_sequence:
#   print(i)
#   if i == item_to_find:
    
#     item_found = True
#     break
    
#   else:
#     item_found = False

# if item_found == True:
#   print("Item found")
# else:
#   print("Item not found")


















# # 10. Simulación de login






# # Enunciado:
# # Guarda un usuario y contraseña en un programa.
# # El usuario tiene 3 intentos para escribirlos correctamente.

# # Output esperado:

# # Usuario: admin
# # Contraseña: 1234
# # Acceso concedido.


# # O si falla:

# # Usuario: admin
# # Contraseña: 1111
# # Datos incorrectos. Intentos restantes: 2



# Write code below 💖
import random


# def fortune():  
#   elhueso = random.randint(1,9)
  
#   elhueso = int(input("Ingresa un número del 1 al 9: "))
#   if elhueso == 1:
#     print("Don't pursue happiness – create it.")
#   elif elhueso == 2:
#     print("All things are difficult before they are easy.")
#   elif elhueso == 3:
#     print("The early bird gets the worm, but the second mouse gets the cheese.")
#   elif elhueso == 4:
#     print("Someone in your life needs a letter from you.")
#   elif elhueso == 5:
#     print("Don't just think. Act!")
#   elif elhueso == 6:
#     print("Your heart will skip a beat.")
#   elif elhueso == 7:
#     print("The fortune you search for is in another cookie.")
#   elif elhueso == 8:
#     print("Help! I'm being held prisoner in a Chinese bakery!")
#   elif elhueso == 9:
#     print("Mensaje 9 vacío o personalizado si lo quieres.")
#   else:
#     print("Número fuera de rango. Debe ser del 1 al 9.")

# def distance_to_miles(distance):
#   miles = 0
#   miles = distance/1.609
#   print(miles)

# distance_to_miles(10000)
# Write code below 💖
# import math
# menu = ['🍔 Cheeseburger','🍟 Fries','🥤 Soda','🍦 Ice Cream','🍪 Cookie']

# def welcome():
#   menu = ['🍔 Cheeseburger','🍟 Fries','🥤 Soda','🍦 Ice Cream','🍪 Cookie']
#   print(f"""elige el item que quieras del menu 
# {menu}""")

# def get_item(x):
#   menu = ['🍔 Cheeseburger','🍟 Fries','🥤 Soda','🍦 Ice Cream','🍪 Cookie']
#   x = x-1
#   return menu[x]



# pedido = []
# x = 0
# welcome()
# try:
#   while x != 67:
#     x =math.floor(int(input("""
#     Elige que item del menu quieres,
#     si deseas dejar de ordenar ingresa 67: """)))
#     if x < len(menu)+1:
#       pedido.append(get_item(x))
#       print(f"Los items que has pedido son:{pedido}")
#     elif x < len(menu)+1 and x != 67:
#       print("error, solo tenemos items del 1 al 5")
# except ValueError as xd:
#   print("""error papi, no se pueden ingresar letras ni simbolos,
#    ahora empieza desde cero klk, mete numeros enteros""")


# class Restaurant:
#   nombre = "bobs burgers"
#   nombre2 = "american diner"
#   puntuacion = 4.7
#   estado = False



# print(vars(Restaurant))

#------------------------------------------------------------------------------------------

# class BankAccount:
#   def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
#     self.first_name = first_name
#     self.last_name = last_name
#     self.account_id = account_id
#     self.account_type = account_type
#     self.pin = pin
#     self.balance = balance

#   def deposito(self, ingresa):
#     self.balance += ingresa
#     print(f"El balance que ingresaras es de {self.balance}")

#   def retirar(self, saca):
#     self.balance -= saca
#     print(f"El balance que sacaras es de {self.balance}")

#   def mirar(self):
#     print(f"""El balance actual es de {self.balance}""")

# CuentaElmer = BankAccount("Elmer", "Lopez", 0, "Ahorro", 1234, 100.00)

# CuentaElmer.deposito(95.00)
# CuentaElmer.retirar(25.00)
# CuentaElmer.mirar()
# print(vars(CuentaElmer))

#--------------------------------------------------------------------------------------

class Pokemon():
  def __init__(self, entry, name, types, description, is_caught):
    self.entry = entry
    self.name = name
    self.types = types
    self.description = description
    self.is_caught = is_caught

  def speak(self):
    print(self.name[0:4]+"-"+self.name)

  def mostrar_detalles(self):
    print(f"""
Entry Number: {self.entry}
Name: {self.name}
Type: {self.types}
Description: {self.description}
""")

Pokemon1 = Pokemon(1,"Pikachu" ,"electrico" ,"La jodida rata" ,True)
Pokemon2 = Pokemon(2, "Greninja", "agua/siniestro", "El ninja anfibio", True)

Pokemon1.speak()
Pokemon1.mostrar_detalles()

Pokemon2.speak()
Pokemon2.mostrar_detalles()

#----------------------------------------------------------------------------------------------------