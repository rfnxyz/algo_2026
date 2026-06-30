from queue_ import Queue
from stack import Stack
from list_ import List
from super_heroes_data import superheroes

# Listado ordenado de manera ascendente (A-Z) por nombre de los personajes

#def orden_alfabetico_asc(listado):
#    self = List()
#    self.sort_by_criterion(name)

def busqueda_thing_raccoon(listado):
    for i in range(1, len(listado)):
        if listado[i]["name"] == "The Thing":
            print(f"{listado[i]["name"]} se ubica en la posición {i}")
        if listado[i]["name"] == "Rocket Raccoon":
            print(f"{listado[i]["name"]} se ubica en la posición {i}")
        
def lista_villanos(listado):
    aux1 = Stack()
    for i in range(0, len(listado)):
        obj = listado[i]
        if listado[i]["is_villain"] == True:
            aux1.push(obj["name"])
    print(f"Listado de superhéroes:")
    print(aux1.show())

def villanos_1980(self):
    aux2 = Queue()
    for i in range(0, len(self)):
        obj = self[i]
        if self[i]["is_villain"] == True and self[i]["first_appearance"] <= 1980:
            aux2.arrive(obj["name"])
            aux2.arrive(obj["first_appearance"])
    print(f"Listado de superhéroes cuya primera aparicion fue antes o durante 1980:")
    print(aux2.show())

# def superheroes_bl_g_my_w(listado):

# def nombres_reales_pjs(listado):

# def superheroes_aparicion(listado):

# def mod_nom_ant_lang(listado):

# def bio_tts(listado):

# def del_ele_zem(listado):

#orden_alfabetico_asc(superheroes)
lista_villanos(superheroes)
villanos_1980(superheroes)
busqueda_thing_raccoon(superheroes)