from queue_ import Queue
from stack import Stack
from list_ import List
from super_heroes_data import superheroes

# Listado ordenado de manera ascendente (A-Z) por nombre de los personajes

def orden_alfabetico_asc(listado):
    print("listado por nombre:")
    orden = sorted(listado, key=lambda h: h["name"])
    for h in orden:
        print(f"{h["name"]}")

# buscar the thing y rocket raccoon
def busqueda_thing_raccoon(listado):
    print("posicion thing raccoon")
    orden = sorted(listado, key=lambda h:["name"])
    for i, h in enumerate(orden):
        if h["name"] in ["The Thing", "Rocket Raccoon"]:
            print(f"{h['name']}: posición {i+1}")

# listado villanos
def lista_villanos(listado):
    print("villanos:")
    for h in listado:
        if h["is_villain"]:
            print(f"{h["name"]}")

# villanos pre-1980
def villanos_1980(listado):
    print("villanos pre-1980:")
    cola = Queue()
    for h in listado:
        if h["is_villain"]:
            cola.arrive(h) # carga
    
    print(f"total villanos en cola: {cola.size()}")
    for p in range(cola.size()):
        villano = cola.move_to_end() # recorre y filtra
        if villano["first_appearance"] < 1980:
            print(f"{villano['name']} ({villano['first_appearance']})")

# heroes que comienzan con 'bl' 'g' 'my' y 'w'
def filtro_prefijo(listado):
    print("heroes bl,g,my,w")
    prefijos = ("Bl", "G", "My", "W")
    for h in listado:
        if h["name"].startswith(prefijos):
            print(f"{h['name']}")

# nombres reales
def nombres_reales_pjs(listado):
    print("orden nombre real")
    orden = sorted(listado, key=lambda h: h["real_name"] or "") # "" a falta de nombre en lista
    for h in orden:
        print(f"{h['real_name']}, ({h['name']})")

# orden aparicion
def superheroes_aparicion(listado):
    print("orden fecha aparicion:")
    orden = sorted(listado, key=lambda h: h["first_appearance"])
    for h in orden:
        print(f"{h['first_appearance']}, {h['name']}")

# modificar ant man
def mod_nom_ant_lang(listado):
    print("modificar nombre real antman")
    for h in listado:
        if h["name"] == "Ant Man":
            h["real_name"] = "Scott Lang"
            print(f"nombre real actualizado a {h['real_name']}")
            return
        if h["real_name"] is None:
            print(f"Sin nombre real: {h['name']}")
    print("Ant Man no encontrado")

# filtrado bio palabras "time-travelling" y "suit"
def filtrar_bio(listado):
    print("personaes con 'time-travelling' o 'suit' en bio")
    for h in listado:
        if "time-travelling" in h["short_bio"] or "suit" in h["short_bio"]:
            print(f"{h['name']}: {h['short_bio']}")

# eliminar electro y baron zemo de la base
def del_pj(listado):
    print("eliminar electro y baron zemo")
    a_eliminar = ["Electro", "Baron Zemo"]
    for nombre in a_eliminar:
        for i, h in enumerate(listado):
            if h["name"] == nombre:
                eliminado = listado.pop(i)
                print(f"Eliminado: {eliminado['name']} / "
                    f"Alias: {eliminado['alias']} / "
                    f"Nombre real: {eliminado['real_name']} / "
                    f"Aparicion: {eliminado['first_appearance']}")
                break
        else:
            print(f"'{nombre}' no estaba en la lista")

##############

orden_alfabetico_asc(superheroes)
busqueda_thing_raccoon(superheroes)
lista_villanos(superheroes)
villanos_1980(superheroes)
filtro_prefijo(superheroes)
nombres_reales_pjs(superheroes)
superheroes_aparicion(superheroes)
mod_nom_ant_lang(superheroes)
filtrar_bio(superheroes)
del_pj(superheroes)