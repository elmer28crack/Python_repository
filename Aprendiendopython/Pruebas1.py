# Mayor = None
# Menor = None
# acumulator = 0
# contador = 0


# print("Elmer's app, esta app es basada en la consola")
# print("Para moverte usaras los numeros, solo debes de seguir la sinstrucciones para cualquier opcion que quiaras hacer mmgvaso hijo de la gran puta")



# while True:
#     print(" ")
#     print("1: Ingresar valores")
#     print("2: Resultados de valores")
#     print("0: Salir de la app rapa tu maldita madre")
#     Elecion = input("--> ")

#     if Elecion == "1":
#         print("Aqui ingresaras los numeros que vayas a usar mmgvaso")
#         print("para volver de la opcion ingresar presiona 0 rapatumadre")
#         while True:
#             while True:
#                 try:
#                     numeros = int(input("--> "))
                
#                     break
#                 except ValueError:
#                     print("xd")
                

#             if numeros == 0:
#                 break
            
#             if Mayor == None or Mayor < numeros:
#                 Mayor = numeros
#             if Menor == None or Menor > numeros:
#                 Menor = numeros
#             if numeros == 0:
#                 break
#             contador += 1
#             acumulator += numeros
            
#             print(numeros)

#     if Elecion == "2"and contador > 0:
#         Promedio = acumulator / contador
#         print("El mayor es", Mayor)
#         print("El menor es", Menor)
#         print("El promedio es", Promedio)
#         continue
        
#     elif contador <= 0 and Elecion == "2": 
#         print("Valor/es no ingresado revisar respuesta")
    
#     if Elecion == "0":
#         break



# import tkinter as tk
# from tkinter import messagebox

# # Variables globales
# mayor = None
# menor = None
# acumulador = 0
# contador = 0

# def ingresar_valor():
#     global mayor, menor, acumulador, contador
    
#     dato = entrada.get()
    
#     try:
#         numero = int(dato)
#     except ValueError:
#         messagebox.showerror("Error", "Debe ser un número")
#         return
    
#     if numero == 0:
#         return
    
#     if mayor is None or numero > mayor:
#         mayor = numero
    
#     if menor is None or numero < menor:
#         menor = numero
    
#     acumulador += numero
#     contador += 1

#     entrada.delete(0, tk.END)
#     messagebox.showinfo("OK", f"Número {numero} agregado")

# def mostrar_resultados():
#     if contador == 0:
#         messagebox.showwarning("Aviso", "No hay datos")
#         return
    
#     promedio = acumulador / contador
    
#     resultado = f"""
# Mayor: {mayor}
# Menor: {menor}
# Promedio: {promedio}
# """
#     messagebox.showinfo("Resultados", resultado)

# def reiniciar():
#     global mayor, menor, acumulador, contador
#     mayor = None
#     menor = None
#     acumulador = 0
#     contador = 0
#     messagebox.showinfo("Reset", "Datos reiniciados")

# # Ventana
# ventana = tk.Tk()
# ventana.title("Elmer's App Pro 😏")
# ventana.geometry("300x200")

# # Input
# entrada = tk.Entry(ventana)
# entrada.pack(pady=10)

# # Botones
# btn_ingresar = tk.Button(ventana, text="Ingresar número", command=ingresar_valor)
# btn_ingresar.pack(pady=5)

# btn_resultados = tk.Button(ventana, text="Ver resultados", command=mostrar_resultados)
# btn_resultados.pack(pady=5)

# btn_reset = tk.Button(ventana, text="Reiniciar", command=reiniciar)
# btn_reset.pack(pady=5)

# # Ejecutar app
# ventana.mainloop()