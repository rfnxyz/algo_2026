from tree import BinaryTree
from super_heroes_data import superheroes

# 5) Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Universe (MCU), desarrollar un algoritmo que contemple lo siguiente.

# 5a)

arbol = BinaryTree()
for h in superheroes:
    arbol.insert_node(h["name"], not h["is_villain"])

def inorden(root, action):
    # izq -> raiz -> derecha: orden alf. asc. 
    if root is not None:
        inorden(root.left, action)
        action(root)
        inorden(root.right, action)

def inorden_desc(root, action):
    # derecha -> raiz -> izq: alf. desc. 
    if root is not None:
        inorden_desc(root.right, action)
        action(root)
        inorden_desc(root.left, action)

def contar(root, condicion=None):
    # contar nodos que cumplen condicion
    if root is None:
        return 0
    suma = 1 if (condicion is None or condicion(root)) else 0
    return suma + contar(root.left, condicion) + contar(root.right, condicion)

def mostrar(node):
    print(f"{node.value}")

def mostrar_si_villano(node):
    if not node.other_values:
        print(f"{node.value}")

def mostrar_si_heroe(node):
    if node.other_values:
        print(f"{node.value}")

def mostrar_heroe_con_c(node):
    if node.other_values and node.value.startswith("C"):
        print(f"{node.value}")

# 5b)
print(f"orden villanos")
inorden(arbol.root, mostrar_si_villano)

# 5c)
print(f"heroe con c")
inorden(arbol.root, mostrar_heroe_con_c)

# 5d)
print(f"cantidad heroes en arbol")
print(f"{contar(arbol.root, lambda n: n.other_values)} superhéroes")

# 5e)
def buscar_proximidad(root, texto, resultado):
    # nodos que contienen 'texto'
    if root is not None:
        buscar_proximidad(root.left, texto, resultado)
        if texto in root.value.lower():
            resultado.append(root)
        buscar_proximidad(root.right, texto, resultado)

def recolectar(root, lista):
    # guarda (nombre, es_heroe) en cada nodo en orden
    if root is not None:
        recolectar(root.left, lista)
        lista.append((root.value, root.other_values))
        recolectar(root.right, lista)

def corregir_nombre(arbol, texto, nombre_correcto):
    encontrados = []
    buscar_proximidad(arbol.root, texto.lower(), encontrados)

    if len(encontrados) == 0:
        print(f"No hay coincidencias para '{texto}'.")
        return arbol

    for n in encontrados:
        print(f"Coincidencia: {n.value}")
    viejo = encontrados[0].value

    # arbol se ordena por nombre, al cambiar se reubica el nodo. se reconstruye con el nombre corregido
    datos = []
    recolectar(arbol.root, datos)
    nuevo = BinaryTree()
    for nombre, es_heroe in datos:
        if nombre == viejo:
            nombre = nombre_correcto
        nuevo.insert_node(nombre, es_heroe)

    print(f"'{viejo}' corregido a '{nombre_correcto}'.")
    return nuevo

print(f"corregir dr strange (busq por proximidad)")
arbol = corregir_nombre(arbol, "stran", "Doctor Strange")

# 5f)
print(f"heroes en orden descendente")
inorden_desc(arbol.root, mostrar_si_heroe)

# 5g)
# bosque: dos arboles tanto para heroes como villanos
arbol_heroes = BinaryTree()
arbol_villanos = BinaryTree()

def repartir(nodo):
    if nodo.other_values:
        arbol_heroes.insert_node(nodo.value, True)
    else:
        arbol_villanos.insert_node(nodo.value, False)

inorden(arbol.root, repartir)

print("\n=== g1) Nodos de cada árbol ===")
print(f"  Árbol de superhéroes: {contar(arbol_heroes.root)} nodos")
print(f"  Árbol de villanos:    {contar(arbol_villanos.root)} nodos")

print(f"g2barrido alfabetico")
print(f"heroes")
inorden(arbol_heroes.root, mostrar)
print(f"villanos")
inorden(arbol_villanos.root, mostrar)