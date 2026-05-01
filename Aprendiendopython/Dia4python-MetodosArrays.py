# Métodos para modificar la lista
append(): # Añade un elemento al final.
python
frutas = ["manzana"]
frutas.append("pera") # ["manzana", "pera"]

extend(): Une otra lista al final.
python
nombres = ["Ana"]
nombres.extend(["Luis", "Sol"]) # ["Ana", "Luis", "Sol"]

insert(): Agrega un elemento en una posición específica.
python
letras = ["a", "c"]
letras.insert(1, "b") # ["a", "b", "c"]

remove(): Borra el primer elemento que coincida con el valor.
python
numeros = [1, 2, 3, 2]
numeros.remove(2) # [1, 3, 2]

pop(): Elimina y te devuelve el elemento (por defecto el último).
python
items = ["📱", "💻", "⌚"]
ultimo = items.pop() # items: ["📱", "💻"], ultimo: "⌚"

sort(): Ordena la lista (alfabéticamente o numéricamente).
python
letras = ["c", "a", "b"]
letras.sort() # ["a", "b", "c"]


reverse(): Invierte el orden de los elementos.
python
num = [1, 2, 3]
num.reverse() # [3, 2, 1]
Métodos de información y búsqueda

count(): Cuenta cuántas veces aparece un valor.
python
votos = ["si", "no", "si"]
votos.count("si") # 2

index(): Devuelve la posición de la primera vez que aparece un valor.
python
colores = ["rojo", "azul"]
colores.index("azul") # 1
Métodos de gestión

copy(): Crea una copia de la lista (para no modificar la original).
python
original = [1, 2]
nueva = original.copy()

clear(): Vacía la lista por completo.
python
lista = [1, 2, 3]
lista.clear() # []