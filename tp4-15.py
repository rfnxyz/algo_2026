from list_ import List

# ============================================================
# Clases
# ============================================================

class Pokemon:
    def __init__(self, nombre, nivel, tipo, subtipo):
        self.name = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        return (f"  Pokemon: {self.name} | Nivel: {self.nivel} "
                f"| Tipo: {self.tipo} | Subtipo: {self.subtipo}")

class Entrenador:
    def __init__(self, nombre, torneos, perdidas, ganadas):
        self.name = nombre
        self.torneos = torneos
        self.perdidas = perdidas
        self.ganadas = ganadas
        self.pokemones = List()
        self.pokemones.add_criterion('name', lambda p: p.name)
        self.pokemones.add_criterion('nivel', lambda p: p.nivel)

    def porcentaje_ganadas(self):
        total = self.ganadas + self.perdidas
        return (self.ganadas / total * 100) if total > 0 else 0

    def __str__(self):
        return (f"Entrenador: {self.name} | Torneos: {self.torneos} "
                f"| Ganadas: {self.ganadas} | Perdidas: {self.perdidas} "
                f"| %Ganadas: {self.porcentaje_ganadas():.1f}%")

# ============================================================
# Funciones criterio para lista de entrenadores
# ============================================================

def by_name(item):
    return item.name

def by_torneos(item):
    return item.torneos

# ============================================================
# Datos
# ============================================================

datos = [
    {
        "nombre": "Ash",
        "torneos": 5, "perdidas": 10, "ganadas": 90,
        "pokemones": [
            ("Pikachu",    35, "Eléctrico", "Ninguno"),
            ("Charizard",  80, "Fuego",     "Volador"),
            ("Bulbasaur",  40, "Planta",    "Veneno"),
            ("Tyrantrum",  60, "Roca",      "Dragón"),
        ]
    },
    {
        "nombre": "Misty",
        "torneos": 2, "perdidas": 20, "ganadas": 60,
        "pokemones": [
            ("Starmie",    45, "Agua",      "Psíquico"),
            ("Psyduck",    30, "Agua",      "Ninguno"),
            ("Wingull",    20, "Agua",      "Volador"),
            ("Pikachu",    35, "Eléctrico", "Ninguno"),
        ]
    },
    {
        "nombre": "Brock",
        "torneos": 4, "perdidas": 15, "ganadas": 85,
        "pokemones": [
            ("Onix",       50, "Roca",      "Tierra"),
            ("Geodude",    30, "Roca",      "Tierra"),
            ("Terrakion",  70, "Roca",      "Lucha"),
            ("Vulpix",     35, "Fuego",     "Ninguno"),
        ]
    },
    {
        "nombre": "Gary",
        "torneos": 7, "perdidas": 5, "ganadas": 95,
        "pokemones": [
            ("Blastoise",  80, "Agua",      "Ninguno"),
            ("Umbreon",    65, "Siniestro", "Ninguno"),
            ("Charizard",  80, "Fuego",     "Volador"),
            ("Tyrantrum",  60, "Roca",      "Dragón"),
        ]
    },
    {
        "nombre": "Dawn",
        "torneos": 3, "perdidas": 25, "ganadas": 55,
        "pokemones": [
            ("Piplup",     25, "Agua",      "Ninguno"),
            ("Togekiss",   60, "Hada",      "Volador"),
            ("Leafeon",    50, "Planta",    "Ninguno"),
            ("Wingull",    20, "Agua",      "Volador"),
        ]
    },
    {
        "nombre": "Paul",
        "torneos": 6, "perdidas": 8, "ganadas": 88,
        "pokemones": [
            ("Electivire", 75, "Eléctrico", "Ninguno"),
            ("Torterra",   80, "Planta",    "Tierra"),
            ("Magmortar",  75, "Fuego",     "Ninguno"),
            ("Pikachu",    35, "Eléctrico", "Ninguno"),
        ]
    },
]

lista_entrenadores = List()
lista_entrenadores.add_criterion('name',    by_name)
lista_entrenadores.add_criterion('torneos', by_torneos)

for d in datos:
    e = Entrenador(d["nombre"], d["torneos"], d["perdidas"], d["ganadas"])
    for p in d["pokemones"]:
        e.pokemones.append(Pokemon(p[0], p[1], p[2], p[3]))
    lista_entrenadores.append(e)

# ============================================================
# a) Cantidad de pokémones de un entrenador
# ============================================================

def cantidad_pokemones(lista, nombre):
    print(f"\n=== a) Pokémones de {nombre} ===")
    idx = lista.search(nombre, 'name')
    if idx is not None:
        print(f"  {lista[idx].name} tiene {lista[idx].pokemones.size()} pokémones.")
    else:
        print(f"  No se encontró el entrenador '{nombre}'.")

# ============================================================
# b) Entrenadores con más de 3 torneos ganados
# ============================================================

def mas_de_tres_torneos(lista):
    print("\n=== b) Entrenadores con más de 3 torneos ganados ===")
    encontrado = False
    for e in lista:
        if e.torneos > 3:
            print(f"  {e.name} ({e.torneos} torneos)")
            encontrado = True
    if not encontrado:
        print("  Ningún entrenador supera los 3 torneos.")

# ============================================================
# c) Pokémon de mayor nivel del entrenador con más torneos
# ============================================================

def pokemon_mayor_nivel_mejor_entrenador(lista):
    print("\n=== c) Pokémon de mayor nivel del entrenador con más torneos ===")
    lista.sort_by_criterion('torneos')
    mejor = lista[-1]
    print(f"  Entrenador con más torneos: {mejor.name} ({mejor.torneos})")
    mejor.pokemones.sort_by_criterion('nivel')
    top = mejor.pokemones[-1]
    print(f"  Pokémon de mayor nivel: {top.name} (Nivel {top.nivel})")

# ============================================================
# d) Todos los datos de un entrenador y sus pokémones
# ============================================================

def datos_entrenador(lista, nombre):
    print(f"\n=== d) Datos completos de {nombre} ===")
    idx = lista.search(nombre, 'name')
    if idx is not None:
        e = lista[idx]
        print(f"  {e}")
        for p in e.pokemones:
            print(f"  {p}")
    else:
        print(f"  No se encontró el entrenador '{nombre}'.")

# ============================================================
# e) Entrenadores con más del 79% de batallas ganadas
# ============================================================

def porcentaje_alto(lista):
    print("\n=== e) Entrenadores con más del 79% de batallas ganadas ===")
    encontrado = False
    for e in lista:
        if e.porcentaje_ganadas() > 79:
            print(f"  {e.name}: {e.porcentaje_ganadas():.1f}%")
            encontrado = True
    if not encontrado:
        print("  Ningún entrenador supera el 79%.")

# ============================================================
# f) Entrenadores con pokémones tipo fuego/planta o agua/volador
# ============================================================

def entrenadores_por_tipo(lista):
    print("\n=== f) Entrenadores con fuego/planta o agua/volador ===")
    encontrado = False
    for e in lista:
        for p in e.pokemones:
            tipo = p.tipo.lower()
            subtipo = p.subtipo.lower()
            if ((tipo == "fuego" and subtipo == "planta") or
                (tipo == "planta" and subtipo == "fuego") or
                (tipo == "agua"   and subtipo == "volador") or
                (tipo == "volador" and subtipo == "agua")):
                print(f"  {e.name} → {p.name} ({p.tipo}/{p.subtipo})")
                encontrado = True
                break
    if not encontrado:
        print("  Ningún entrenador cumple la condición.")

# ============================================================
# g) Promedio de nivel de pokémones de un entrenador
# ============================================================

def promedio_nivel(lista, nombre):
    print(f"\n=== g) Promedio de nivel de pokémones de {nombre} ===")
    idx = lista.search(nombre, 'name')
    if idx is not None:
        e = lista[idx]
        total = sum(p.nivel for p in e.pokemones)
        promedio = total / e.pokemones.size()
        print(f"  Promedio de nivel de {e.name}: {promedio:.1f}")
    else:
        print(f"  No se encontró el entrenador '{nombre}'.")

# ============================================================
# h) Cuántos entrenadores tienen un determinado pokémon
# ============================================================

def cuantos_tienen_pokemon(lista, nombre_pokemon):
    print(f"\n=== h) Entrenadores que tienen a {nombre_pokemon} ===")
    contador = 0
    for e in lista:
        for p in e.pokemones:
            if p.name == nombre_pokemon:
                contador += 1
                break
    print(f"  {contador} entrenador(es) tienen a {nombre_pokemon}.")

# ============================================================
# i) Entrenadores con pokémones repetidos entre sus filas
# ============================================================

def entrenadores_con_repetidos(lista):
    print("\n=== i) Entrenadores con pokémones repetidos ===")
    encontrado = False
    for e in lista:
        nombres = []
        for p in e.pokemones:
            if p.name in nombres:
                print(f"  {e.name} tiene repetido a {p.name}.")
                encontrado = True
                break
            nombres.append(p.name)
    if not encontrado:
        print("  Ningún entrenador tiene pokémones repetidos.")

# ============================================================
# j) Entrenadores con Tyrantrum, Terrakion o Wingull
# ============================================================

def entrenadores_con_especificos(lista):
    buscados = ["Tyrantrum", "Terrakion", "Wingull"]
    print(f"\n=== j) Entrenadores con {', '.join(buscados)} ===")
    encontrado = False
    for e in lista:
        for p in e.pokemones:
            if p.name in buscados:
                print(f"  {e.name} → {p.name}")
                encontrado = True
                break
    if not encontrado:
        print("  Ningún entrenador tiene esos pokémones.")

# ============================================================
# k) ¿El entrenador X tiene al pokémon Y?
# ============================================================

def entrenador_tiene_pokemon(lista):
    print("\n=== k) Buscar pokémon de un entrenador ===")
    nombre_e = input("  Ingrese el nombre del entrenador: ")
    nombre_p = input("  Ingrese el nombre del pokémon: ")

    idx = lista.search(nombre_e, 'name')
    if idx is None:
        print(f"  No se encontró el entrenador '{nombre_e}'.")
        return

    e = lista[idx]
    for p in e.pokemones:
        if p.name == nombre_p:
            print(f"  Sí, {e.name} tiene a {nombre_p}.")
            print(f"  {e}")
            print(f"  {p}")
            return

    print(f"  {e.name} no tiene a {nombre_p}.")

# ============================================================
# Programa principal
# ============================================================

cantidad_pokemones(lista_entrenadores, "Ash")
mas_de_tres_torneos(lista_entrenadores)
pokemon_mayor_nivel_mejor_entrenador(lista_entrenadores)
datos_entrenador(lista_entrenadores, "Misty")
porcentaje_alto(lista_entrenadores)
entrenadores_por_tipo(lista_entrenadores)
promedio_nivel(lista_entrenadores, "Brock")
cuantos_tienen_pokemon(lista_entrenadores, "Pikachu")
entrenadores_con_repetidos(lista_entrenadores)
entrenadores_con_especificos(lista_entrenadores)
entrenador_tiene_pokemon(lista_entrenadores)