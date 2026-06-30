from stack import Stack
from list_ import List
from super_heroes_data import superheroes

# Función recursiva, búsqueda Capitán América entre 15 superhéroes
import random
def by_name(item):
    return item.name

def busqueda_cap_am(listado):
    print(f"Selección de 15 superhéroes al azar...")
    aux = Stack()
    while aux.size() != 15:
        objx = random.choice(listado)
        if objx["is_villain"] == False:
            aux.push(objx["name"])
    print(f"Búsqueda de Capitán América dentro de los seleccionados...")
    aux = List()
    aux.add_criterion("name", by_name)
#    for name in aux:
    if aux.search("Captain America") == True:
        print(f"Se encontró a Capitán América dentro de los seleccionados.")
        return True, aux
    else:
        print(f"No se encontró a Capitán América dentro de los seleccionados.")
        return False, aux

def lista_heroes(listado):
    aux1 = Stack()
    for i in range(0, len(listado)):
        obj = listado[i]
        if listado[i]["is_villain"] == False:
            aux1.push(obj["name"])
    print(f"Listado de superhéroes:")
    print(aux1.show())

print(busqueda_cap_am(superheroes))
print(lista_heroes(superheroes))