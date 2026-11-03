import random
import unicodedata
from tree import BinaryTree
from queue_ import Queue

WEAK = {
    "Normal": ["Lucha"], "Fuego": ["Agua", "Tierra", "Roca"],
    "Agua": ["Planta", "Eléctrico"], "Eléctrico": ["Tierra"],
    "Planta": ["Fuego", "Hielo", "Veneno", "Volador", "Bicho"],
    "Hielo": ["Fuego", "Lucha", "Roca", "Acero"],
    "Lucha": ["Volador", "Psíquico", "Hada"],
    "Veneno": ["Tierra", "Psíquico"], "Tierra": ["Agua", "Planta", "Hielo"],
    "Volador": ["Eléctrico", "Hielo", "Roca"],
    "Psíquico": ["Bicho", "Fantasma", "Siniestro"],
    "Bicho": ["Fuego", "Volador", "Roca"],
    "Roca": ["Agua", "Planta", "Lucha", "Tierra", "Acero"],
    "Fantasma": ["Fantasma", "Siniestro"],
    "Dragón": ["Hielo", "Dragón", "Hada"],
    "Siniestro": ["Lucha", "Bicho", "Hada"],
    "Acero": ["Fuego", "Lucha", "Tierra"], "Hada": ["Veneno", "Acero"],
}
RES = {
    "Normal": [], "Fuego": ["Fuego", "Planta", "Hielo", "Bicho", "Acero", "Hada"],
    "Agua": ["Fuego", "Agua", "Hielo", "Acero"],
    "Eléctrico": ["Eléctrico", "Volador", "Acero"],
    "Planta": ["Agua", "Eléctrico", "Planta", "Tierra"], "Hielo": ["Hielo"],
    "Lucha": ["Bicho", "Roca", "Siniestro"],
    "Veneno": ["Planta", "Lucha", "Veneno", "Bicho", "Hada"],
    "Tierra": ["Veneno", "Roca"], "Volador": ["Planta", "Lucha", "Bicho"],
    "Psíquico": ["Lucha", "Psíquico"], "Bicho": ["Planta", "Lucha", "Tierra"],
    "Roca": ["Normal", "Fuego", "Veneno", "Volador"],
    "Fantasma": ["Veneno", "Bicho"],
    "Dragón": ["Fuego", "Agua", "Eléctrico", "Planta"],
    "Siniestro": ["Fantasma", "Siniestro"],
    "Acero": ["Normal", "Planta", "Hielo", "Volador", "Psíquico", "Bicho",
              "Roca", "Dragón", "Acero", "Hada"],
    "Hada": ["Lucha", "Bicho", "Siniestro"],
}
IMMUN = {
    "Normal": ["Fantasma"], "Volador": ["Tierra"], "Tierra": ["Eléctrico"],
    "Fantasma": ["Normal", "Lucha"], "Siniestro": ["Psíquico"],
    "Acero": ["Veneno"], "Hada": ["Dragón"],
}

def calcular_debilidades(tipos): # ataque y multiplicador
    debilidades = []
    for atk in WEAK:
        mult = 1.0
        for t in tipos:
            if atk in IMMUN.get(t, []):
                mult = 0
            elif atk in WEAK[t]:
                mult *= 2
            elif atk in RES[t]:
                mult *= 0.5
        if mult > 1:
            debilidades.append(atk)
    return debilidades

# database : (numero, nombre, tipos, flags)
    # flags : M = megaevol. G = gigamax

DATABASE = [
    (1, "Bulbasaur", "Planta/Veneno", ""), (2, "Ivysaur", "Planta/Veneno", ""),
    (3, "Venusaur", "Planta/Veneno", "MG"), (4, "Charmander", "Fuego", ""),
    (5, "Charmeleon", "Fuego", ""), (6, "Charizard", "Fuego/Volador", "MG"),
    (7, "Squirtle", "Agua", ""), (8, "Wartortle", "Agua", ""),
    (9, "Blastoise", "Agua", "MG"), (12, "Butterfree", "Bicho/Volador", "G"),
    (15, "Beedrill", "Bicho/Veneno", "M"), (18, "Pidgeot", "Normal/Volador", "M"),
    (25, "Pikachu", "Eléctrico", "G"), (26, "Raichu", "Eléctrico", ""),
    (37, "Vulpix", "Fuego", ""), (38, "Ninetales", "Fuego", ""),
    (52, "Meowth", "Normal", "G"), (54, "Psyduck", "Agua", ""),
    (59, "Arcanine", "Fuego", ""), (63, "Abra", "Psíquico", ""),
    (64, "Kadabra", "Psíquico", ""), (65, "Alakazam", "Psíquico", "M"),
    (68, "Machamp", "Lucha", "G"), (74, "Geodude", "Roca/Tierra", ""),
    (76, "Golem", "Roca/Tierra", ""), (79, "Slowpoke", "Agua/Psíquico", ""),
    (80, "Slowbro", "Agua/Psíquico", "M"), (92, "Gastly", "Fantasma/Veneno", ""),
    (93, "Haunter", "Fantasma/Veneno", ""), (94, "Gengar", "Fantasma/Veneno", "MG"),
    (95, "Onix", "Roca/Tierra", ""), (99, "Kingler", "Agua", "G"),
    (104, "Cubone", "Tierra", ""), (115, "Kangaskhan", "Normal", "M"),
    (123, "Scyther", "Bicho/Volador", ""), (127, "Pinsir", "Bicho", "M"),
    (129, "Magikarp", "Agua", ""), (130, "Gyarados", "Agua/Volador", "M"),
    (131, "Lapras", "Agua/Hielo", "G"), (133, "Eevee", "Normal", "G"),
    (134, "Vaporeon", "Agua", ""), (135, "Jolteon", "Eléctrico", ""),
    (136, "Flareon", "Fuego", ""), (142, "Aerodactyl", "Roca/Volador", "M"),
    (143, "Snorlax", "Normal", "G"), (144, "Articuno", "Hielo/Volador", ""),
    (145, "Zapdos", "Eléctrico/Volador", ""), (146, "Moltres", "Fuego/Volador", ""),
    (147, "Dratini", "Dragón", ""), (149, "Dragonite", "Dragón/Volador", ""),
    (150, "Mewtwo", "Psíquico", "M"), (151, "Mew", "Psíquico", ""),
    (152, "Chikorita", "Planta", ""), (155, "Cyndaquil", "Fuego", ""),
    (158, "Totodile", "Agua", ""), (181, "Ampharos", "Eléctrico", "M"),
    (196, "Espeon", "Psíquico", ""), (197, "Umbreon", "Siniestro", ""),
    (208, "Steelix", "Acero/Tierra", "M"), (212, "Scizor", "Bicho/Acero", "M"),
    (214, "Heracross", "Bicho/Lucha", "M"), (228, "Houndour", "Siniestro/Fuego", ""),
    (229, "Houndoom", "Siniestro/Fuego", "M"), (245, "Suicune", "Agua", ""),
    (248, "Tyranitar", "Roca/Siniestro", "M"), (249, "Lugia", "Psíquico/Volador", ""),
    (250, "Ho-Oh", "Fuego/Volador", ""), (252, "Treecko", "Planta", ""),
    (254, "Sceptile", "Planta", "M"), (255, "Torchic", "Fuego", ""),
    (257, "Blaziken", "Fuego/Lucha", "M"), (258, "Mudkip", "Agua", ""),
    (260, "Swampert", "Agua/Tierra", "M"), (282, "Gardevoir", "Psíquico/Hada", "M"),
    (302, "Sableye", "Siniestro/Fantasma", "M"), (303, "Mawile", "Acero/Hada", "M"),
    (306, "Aggron", "Acero/Roca", "M"), (310, "Manectric", "Eléctrico", "M"),
    (354, "Banette", "Fantasma", "M"), (359, "Absol", "Siniestro", "M"),
    (373, "Salamence", "Dragón/Volador", "M"), (376, "Metagross", "Acero/Psíquico", "M"),
    (384, "Rayquaza", "Dragón/Volador", "M"), (387, "Turtwig", "Planta", ""),
    (390, "Chimchar", "Fuego", ""), (393, "Piplup", "Agua", ""),
    (445, "Garchomp", "Dragón/Tierra", "M"), (448, "Lucario", "Lucha/Acero", "M"),
    (468, "Togekiss", "Hada/Volador", ""), (475, "Gallade", "Psíquico/Lucha", "M"),
    (483, "Dialga", "Acero/Dragón", ""), (484, "Palkia", "Agua/Dragón", ""),
    (487, "Giratina", "Fantasma/Dragón", ""), (495, "Snivy", "Planta", ""),
    (498, "Tepig", "Fuego", ""), (501, "Oshawott", "Agua", ""),
    (571, "Zoroark", "Siniestro", ""), (609, "Chandelure", "Fantasma/Fuego", ""),
    (635, "Hydreigon", "Siniestro/Dragón", ""), (643, "Reshiram", "Dragón/Fuego", ""),
    (644, "Zekrom", "Dragón/Eléctrico", ""), (650, "Chespin", "Planta", ""),
    (653, "Fennekin", "Fuego", ""), (656, "Froakie", "Agua", ""),
    (658, "Greninja", "Agua/Siniestro", ""), (697, "Tyrantrum", "Roca/Dragón", ""),
    (700, "Sylveon", "Hada", ""), (706, "Goodra", "Dragón", ""),
    (722, "Rowlet", "Planta/Volador", ""), (725, "Litten", "Fuego", ""),
    (728, "Popplio", "Agua", ""), (745, "Lycanroc", "Roca", ""),
    (778, "Mimikyu", "Fantasma/Hada", ""), (810, "Grookey", "Planta", ""),
    (812, "Rillaboom", "Planta", "G"), (813, "Scorbunny", "Fuego", ""),
    (815, "Cinderace", "Fuego", "G"), (816, "Sobble", "Agua", ""),
    (818, "Inteleon", "Agua", "G"), (823, "Corviknight", "Volador/Acero", "G"),
    (849, "Toxtricity", "Eléctrico/Veneno", "G"), (884, "Duraludon", "Acero/Dragón", "G"),
    (906, "Sprigatito", "Planta", ""), (908, "Meowscarada", "Planta/Siniestro", ""),
    (909, "Fuecoco", "Fuego", ""), (911, "Skeledirge", "Fuego/Fantasma", ""),
    (912, "Quaxly", "Agua", ""), (914, "Quaquaval", "Agua/Lucha", ""),
    (937, "Ceruledge", "Fuego/Fantasma", ""), (979, "Annihilape", "Lucha/Fantasma", ""),
    (1000, "Gholdengo", "Acero/Fantasma", ""), (1007, "Koraidon", "Lucha/Dragón", ""),
    (1008, "Miraidon", "Eléctrico/Dragón", ""),
]

def normalizar(texto): # no discriminar mayusculs o tildes
    sin = unicodedata.normalize("NFD", texto)
    return "".join(c for c in sin if unicodedata.category(c) != "Mn").lower().strip()

# carga arboles

arbol_nombre = BinaryTree()
arbol_numero = BinaryTree()
arbol_tipo = BinaryTree()

orden_carga = list(DATABASE)
random.seed(2026)
random.shuffle(orden_carga) # aleatorio

for numero, nombre, tipos, flags in orden_carga:
    lista_tipos = tipos.split("/")
    pokemon = {
        "numero": numero,
        "nombre": nombre,
        "tipos": lista_tipos,
        "debilidades": calcular_debilidades(lista_tipos),
        "mega": "M" in flags,
        "gigamax": "G" in flags,
    }
    arbol_nombre.insert_node(nombre, pokemon)
    arbol_numero.insert_node(numero, pokemon)
    for tipo in lista_tipos:
        clave = normalizar(tipo)
        nodo = arbol_tipo.search(clave)
        if nodo is None:
            arbol_tipo.insert_node(clave, {"tipo": tipo, "pokemones": [pokemon]})
        else:
            nodo.other_values["pokemones"].append(pokemon)

# recorridos recursivos

def inorden(root, accion):
    if root is not None:
        inorden(root.left, accion)
        accion(root)
        inorden(root.right, accion)

def contar(root, condicion):
    if root is None:
        return 0
    suma = 1 if condicion(root) else 0
    return suma + contar(root.left, condicion) + contar(root.right, condicion)

def mostrar_pokemon(p):
    print(f"num. {p['numero']} - {p['nombre']}")
    print(f"tipo: {', '.join(p['tipos'])}")
    print(f"debilidad: {', '.join(p['debilidades'])}")
    print(f"megaevolucion: {'Si' if p['mega'] else 'No'}")
    print(f"gigamax: {'Si' if p['gigamax'] else 'No'}")

# consultas

print(f"pokemon cargados: {contar(arbol_nombre.root, lambda n: True)}")

# busqueda por numero

print(f"datos a partir de numero")
for numero in (25, 6, 999):
    nodo = arbol_numero.search(numero)
    if nodo is None:
        print(f"no hay pokemon con el numero {numero}.")
    else:
        mostrar_pokemon(nodo.other_values)

# busqueda por proximidad

def buscar_prox(arbol, texto):
    texto = texto.lower()
    found = []
    inorden(arbol.root, lambda n: found.append(n.other_values) if texto in n.value.lower() else None)
    return found

print(f"datos a partir de proximidad")
for texto in ("bul", "char"):
    print(f"Busqueda '{texto}:")
    resultado = buscar_prox(arbol_nombre, texto)
    if not resultado:
        print("sin coincidencias")
    for p in resultado:
        mostrar_pokemon(p)

# busqueda por tipo

def buscar_tipo(arbol, tipo):
    nodo = arbol.search(normalizar(tipo))
    if nodo is None:
        print(f"no hay pokemon de tipo {tipo}.")
        return
    lista = sorted(p["nombre"] for p in nodo.other_values["pokemones"])
    print(f"{nodo.other_values['tipo']} ({len(lista)}): {', '.join(lista)}")

print(f"pokemon por tipo")
for tipo in ("Fantasma", "Fuego", "Acero", "Electrico"):
    buscar_tipo(arbol_tipo, tipo)

# listados ascendentes

print(f"list. asc. por numero")
inorden(arbol_numero.root, lambda n: print(f"num. {n.value} {n.other_values['nombre']}"))

print("list. asc. por nombre")
inorden(arbol_nombre.root, lambda n: print(f"{n.value}"))

def listar_nivel(arbol):
    cola = Queue()
    if arbol.root is not None:
        cola.arrive((arbol.root, 0))
    nivel_actual = -1
    linea = []
    while cola.size() > 0:
        nodo, nivel = cola.attention()
        if nivel != nivel_actual:
            if linea:
                print(f"nivel {nivel_actual}: {', '.join(linea)}")
            nivel_actual = nivel
            linea = []
        linea.append(nodo.value)
        if nodo.left is not None:
            cola.arrive((nodo.left, nivel + 1))
        if nodo.right is not None:
            cola.arrive((nodo.right, nivel + 1))
    if linea:
        print(f"nivel {nivel_actual}: {', '.join(linea)}")

print("listado por nivel (arbol por nombre)")
listar_nivel(arbol_nombre)

# debiles frente a jolteon, lycanroc y tyrantrum
def debil_a(arbol, atk):
    for nombre in atk:
        nodo = arbol.search(nombre)
        if nodo is None:
            print(f"{nombre} no esta cargado")
            continue
        tipos_atk = nodo.other_values["tipos"]
        print(f"debiles frente a {nombre} (tipo {'/'.join(tipos_atk)}):")
        resultado = []
        def revisar(n):
            p = n.other_values
            golpe = [t for t in tipos_atk if t in p["debilidades"]]
            if golpe:
                resultado.append(f"{p['nombre']} {', '.join(golpe)}")
            inorden(arbol.root, revisar)
            print(f"{len(resultado)} pokemon: {', '.join(resultado) if resultado else '-'}")

print("pokemones debiles frente a jolteon, lycanroc y tyrantrum")
debil_a(arbol_nombre, ["Jolteon", "Lycanroc", "Tyrantrum"])

# tipos y cantidad de cada uno

print(f"tipos de pokemon y cantidad de c/u")
inorden(arbol_tipo.root, lambda n: print(f"{n.other_values['tipo']}: {len(n.other_values['pokemones'])}"))

# megaevol y gigamax

print(f"megaevolucion y gigamax")
print(f"con meaevolucion: {contar(arbol_nombre.root, lambda n: n.other_values['mega'])}")
print(f"con igamax: {contar(arbol_nombre.root, lambda n: n.other_values['gigamax'])}")