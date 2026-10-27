from stack import Stack
from list_ import List
from super_heroes_data import superheroes

# Función recursiva, búsqueda Capitán América entre 15 superhéroes
import random
## seleccion de 15
lista_15 = []
elegidos = [h for h in superheroes if not h["is_villain"]]
while len(lista_15) < 15:
    objx = random.choice(elegidos)
    if objx["name"] not in lista_15:
        lista_15.append(objx["name"])

## busq cap am
def busqueda_cap_am(lista, indice=0):
    if indice == len(lista):
        return False
    if lista[indice] == "Captain America":
        return True
    return busqueda_cap_am(lista, indice+1)

## lista
def lista_heroes(lista, indice=0):
    if indice == len(lista):
        return
    print(f"{indice+1}, {lista[indice]}")
    lista_heroes(lista, indice+1)

###

print("seleccion de 15")
lista_heroes(lista_15)
print("busq capitan america")
if busqueda_cap_am(lista_15):
    print("se encontro al capitan america entre los 15")
else:
    print("NO se encontro al capitan america")