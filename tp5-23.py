##### 23) 

from tree import BinaryTree
from queue_ import Queue

# Datos de la tabla: (criatura, derrotada por)
# -> None = "-"

tabla = [
    ("Ceto", None), ("Cerda de Cromión", "Teseo"), ("Tifón", "Zeus"),
    ("Ortro", "Heracles"), ("Equidna", "Argos Panoptes"),
    ("Toro de Creta", "Teseo"), ("Dino", None),
    ("Jabalí de Calidón", "Atalanta"), ("Prefredo", None),
    ("Carcinos", None), ("Enio", None), ("Gerión", "Heracles"),
    ("Escila", None), ("Cloto", None), ("Caribdis", None),
    ("Láquesis", None), ("Euriale", None), ("Átropos", None),
    ("Esteno", None), ("Minotauro de Creta", "Teseo"),
    ("Medusa", "Perseo"), ("Harpías", None), ("Ladón", "Heracles"),
    ("Argos Panoptes", "Hermes"), ("Águila de Cáucaso", None),
    ("Aves del Estínfalo", None), ("Quimera", "Belerofonte"),
    ("Talos", "Medea"), ("Hidra de Lerna", "Heracles"), ("Sirenas", None),
    ("León de Nemea", "Heracles"), ("Pitón", "Apolo"),
    ("Esfinge", "Edipo"), ("Cierva de Cerinea", None),
    ("Dragón de la Cólquida", None), ("Basilisco", None),
    ("Cerbero", None), ("Jabalí de Erimato", None),
]

# Cada nodo:
# valor = nombre de la criatura
# other_values = {derrotado_por, descripcion,
# capturada}

arbol = BinaryTree()
for criatura, heroe in tabla:
    arbol.insert_node(criatura, {
        "derrotado_por": heroe,
        "descripcion": "",
        "capturada": None,       
        # g) héroe o dios que la capturó
    })

# Recorridos y utilidades recursivas

def inorden(root, accion):
    if root is not None:
        inorden(root.left, accion)
        accion(root)
        inorden(root.right, accion)

def recolectar(root, lista):
    # Guarda datos de cada nodo, en orden
    if root is not None:
        recolectar(root.left, lista)
        lista.append((root.value, root.other_values))
        recolectar(root.right, lista)

def texto_nodo(nodo):
    d = nodo.other_values
    return (f"{nodo.value} | Derrotada por: {d['derrotado_por'] or '-'} "
            f"| Capturada por: {d['capturada'] or '-'}")

# a) Listado inorden de criaturas y quién las derrotó

# Criaturas (inorden) y quién las derrotó
inorden(arbol.root, lambda n: print(
    f"  {n.value} -> {n.other_values['derrotado_por'] or '-'}"))

# b) Cargar una breve descripción sobre cada criatura

def cargar_descripcion(arbol, criatura, descripcion):
    nodo = arbol.search(criatura)
    if nodo is None:
        print(f"  No se encontró '{criatura}'.")
    else:
        nodo.other_values["descripcion"] = descripcion

# Descripciones
cargar_descripcion(arbol, "Talos", "Gigante de bronce que custodiaba la isla de Creta.")
cargar_descripcion(arbol, "Cerbero", "Perro de tres cabezas que guarda las puertas del Hades.")
cargar_descripcion(arbol, "Hidra de Lerna", "Serpiente acuática de múltiples cabezas que se regeneraban.")
cargar_descripcion(arbol, "Medusa", "Gorgona cuya mirada convertía en piedra.")
cargar_descripcion(arbol, "Ladón", "Dragón que custodiaba las manzanas de oro del jardín de las Hespérides.")
print("  Descripciones cargadas (Talos, Cerbero, Hidra de Lerna, Medusa, Ladón).")

# c) Información de Talos

talos = arbol.search("Talos")
if talos is not None:
    print(f"  Criatura:      {talos.value}")
    print(f"  Derrotada por: {talos.other_values['derrotado_por'] or '-'}")
    print(f"  Capturada por: {talos.other_values['capturada'] or '-'}")
    print(f"  Descripción:   {talos.other_values['descripcion'] or '-'}")
else:
    print("  Talos no está en el árbol.")

# d) Los 3 héroes o dioses que derrotaron más criaturas

def contar_derrotas(root, conteo):
    if root is not None:
        contar_derrotas(root.left, conteo)
        h = root.other_values["derrotado_por"]
        if h is not None:
            conteo[h] = conteo.get(h, 0) + 1
        contar_derrotas(root.right, conteo)

conteo = {}
contar_derrotas(arbol.root, conteo)
ranking = sorted(conteo.items(), key=lambda x: (-x[1], x[0]))
corte = ranking[2][1]                                   
# derrotas del 3.er lugar
claros = [(h, c) for h, c in ranking if c > corte]      
# puestos sin empate
empatados = [h for h, c in ranking if c == corte]      
# grupo del corte

for puesto, (heroe, cant) in enumerate(claros, start=1):
    print(f"  {puesto}. {heroe}: {cant} criatura(s)")

if len(claros) + len(empatados) <= 3:
    for puesto, heroe in enumerate(empatados, start=len(claros) + 1):
        print(f"  {puesto}. {heroe}: {corte} criatura(s)")
else:
    print(f"  {len(claros) + 1}.º en adelante: empate de {len(empatados)} con "
          f"{corte} criatura(s) cada uno:")
    print(f"     {', '.join(empatados)}")

# e) Criaturas derrotadas por Heracles

inorden(arbol.root, lambda n: print(f"  {n.value}")
        if n.other_values["derrotado_por"] == "Heracles" else None)

# f) Criaturas que no han sido derrotadas

inorden(arbol.root, lambda n: print(f"  {n.value}")
        if n.other_values["derrotado_por"] is None else None)

# g) Campo "capturada": ya existe en cada nodo
# (valor inicial None)
# h) Heracles capturó a Cerbero, Toro de Creta,
# Cierva de Cerinea y Jabalí de Erimato

for nombre in ["Cerbero", "Toro de Creta", "Cierva de Cerinea", "Jabalí de Erimato"]:
    nodo = arbol.search(nombre)
    if nodo is not None:
        nodo.other_values["capturada"] = "Heracles"
        print(f"  {nombre}: capturada por Heracles.")
    else:
        print(f"  No se encontró '{nombre}'.")

# i) Búsqueda por coincidencia

def buscar_coincidencia(root, texto, resultado):
    if root is not None:
        buscar_coincidencia(root.left, texto, resultado)
        if texto in root.value.lower():
            resultado.append(root)
        buscar_coincidencia(root.right, texto, resultado)

def buscar(arbol, texto):
    print(f"  Búsqueda '{texto}':")
    encontrados = []
    buscar_coincidencia(arbol.root, texto.lower(), encontrados)
    if not encontrados:
        print("    Sin coincidencias.")
    for n in encontrados:
        print(f"    {texto_nodo(n)}")

buscar(arbol, "cer")
buscar(arbol, "jabal")

# ============================================================
# j) Eliminar Basilisco y Sirenas
# ============================================================

def eliminar_criaturas(arbol, nombres):
    datos = []
    recolectar(arbol.root, datos)
    nuevo = BinaryTree()
    for nombre, info in datos:
        if nombre in nombres:
            print(f"  Eliminada: {nombre}")
        else:
            nuevo.insert_node(nombre, info)
    return nuevo

arbol = eliminar_criaturas(arbol, ["Basilisco", "Sirenas"])

# k) Aves del Estínfalo: Heracles derrotó a varias

aves = arbol.search("Aves del Estínfalo")
if aves is not None:
    aves.other_values["derrotado_por"] = "Heracles"
    aves.other_values["descripcion"] = (aves.other_values["descripcion"]
                                        + " Heracles derrotó a varias.").strip()
    print(f"  {texto_nodo(aves)}")
    print(f"  Descripción: {aves.other_values['descripcion']}")

# ============================================================
# l) Ladón -> Dragón Ladón
# ============================================================

def renombrar(arbol, viejo, nuevo_nombre):
    datos = []
    recolectar(arbol.root, datos)
    nuevo = BinaryTree()
    for nombre, info in datos:
        nuevo.insert_node(nuevo_nombre if nombre == viejo else nombre, info)
    return nuevo

if arbol.search("Ladón") is not None:
    arbol = renombrar(arbol, "Ladón", "Dragón Ladón")
    print(f"  Ahora: {texto_nodo(arbol.search('Dragón Ladón'))}")
else:
    print("  Ladón no está en el árbol.")

# m) Listado por nivel (usa una cola)

pendientes = Queue()
if arbol.root is not None:
    pendientes.arrive((arbol.root, 0))
nivel_actual = -1
while pendientes.size() > 0:
    nodo, nivel = pendientes.attention()
    if nivel != nivel_actual:
        nivel_actual = nivel
        print(f"  -- Nivel {nivel} --")
    print(f"    {nodo.value}")
    if nodo.left is not None:
        pendientes.arrive((nodo.left, nivel + 1))
    if nodo.right is not None:
        pendientes.arrive((nodo.right, nivel + 1))

# n) Criaturas capturadas por Heracles

inorden(arbol.root, lambda n: print(f"  {n.value}")
        if n.other_values["capturada"] == "Heracles" else None)