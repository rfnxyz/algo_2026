from graph import Graph

# (nombre, tipo) según la figura
EQUIPOS = [
    ("Red Hat", "notebook"), ("Debian", "notebook"), ("Arch", "notebook"),
    ("Guaraní", "servidor"), ("MongoDB", "servidor"),
    ("Router 1", "router"), ("Router 2", "router"), ("Router 3", "router"),
    ("Switch 1", "switch"), ("Switch 2", "switch"),
    ("Manjaro", "pc"), ("Parrot", "pc"), ("Fedora", "pc"),
    ("Ubuntu", "pc"), ("Mint", "pc"),
    ("Impresora", "impresora"),
]

# (origen, destino, peso) según la figura
CONEXIONES = [
    ("Red Hat", "Router 2", 25), ("Guaraní", "Router 2", 9),
    ("Router 2", "Router 3", 50), ("Router 2", "Router 1", 37),
    ("Router 3", "Router 1", 43), ("Router 3", "Switch 2", 61),
    ("Manjaro", "Switch 2", 40), ("Parrot", "Switch 2", 12),
    ("MongoDB", "Switch 2", 5), ("Fedora", "Switch 2", 3),
    ("Arch", "Switch 2", 56), ("Debian", "Switch 1", 17),
    ("Ubuntu", "Switch 1", 18), ("Router 1", "Switch 1", 29),
    ("Impresora", "Switch 1", 22), ("Mint", "Switch 1", 80),
]

def cargar(conexiones):
    g = Graph(is_dir=False)
    for nombre, tipo in EQUIPOS:
        g.add_vertex(nombre, {"tipo": tipo})
    for a, b, peso in conexiones:
        g.add_edge(peso, a, b)
    return g

def tipo_de(g, nombre):
    for v in g:
        if v.value == nombre:
            return v.other_values["tipo"]

def camino(g, origen, destino):
    ruta, costo = g.camino_mas_corto(origen, destino)
    if ruta is None:
        print(f"  {origen} -> {destino}: sin camino")
    else:
        print(f"  {origen} -> {destino}: {' -> '.join(ruta)} (costo {costo})")
    return costo

# a) equipos y tipos

if __name__ == "__main__":
    g = cargar(CONEXIONES)

    for v in g:
        print(f"  {v.value}: {v.other_values['tipo']}")

# b) baridos desde las notebooks (profundidad y amplitud)
    for nb in ("Red Hat", "Debian", "Arch"):
        print(f"  -- Profundidad desde {nb} --")
        g.deep_show(nb)
        print(f"  -- Amplitud desde {nb} --")
        g.amplitude_show(nb)

# c) camino más corto a la impresora 
    for pc in ("Manjaro", "Red Hat", "Fedora"):
        camino(g, pc, "Impresora")

# d) árbol de expansión mínimo
    aristas, total = g.prim("Red Hat")
    for a, b, peso in aristas:
        print(f"  {a} -- {b} ({peso})")
    print(f"  Peso total: {total}")

# e) pc más cercana a servidor guaraní
    print("\n=== e) PC más cercana al servidor Guaraní ===")
    mejor = None
    for v in g:
        if v.other_values["tipo"] == "pc":
            costo = camino(g, v.value, "Guaraní")
            if mejor is None or costo < mejor[1]:
                mejor = (v.value, costo)
    print(f"  Respuesta: {mejor[0]} ({mejor[1]})")

# f) computadora del switch 2 más cercana a MongoDB

    conectados = [b if a == "Switch 2" else a
                  for a, b, _ in CONEXIONES if "Switch 2" in (a, b)]
    candidatos = [n for n in conectados if tipo_de(g, n) in ("pc", "notebook")]
    mejor = None
    for nombre in candidatos:
        costo = camino(g, nombre, "MongoDB")
        if mejor is None or costo < mejor[1]:
            mejor = (nombre, costo)
    print(f"  Respuesta: {mejor[0]} ({mejor[1]})")

# g) impresora conectada a router 2

    g2 = cargar([c for c in CONEXIONES if c[0] != "Impresora"]
                + [("Impresora", "Router 2", 22)])
    print("  Barridos desde las notebooks:")
    for nb in ("Red Hat", "Debian", "Arch"):
        print(f"  -- Profundidad desde {nb} --")
        g2.deep_show(nb)
        print(f"  -- Amplitud desde {nb} --")
        g2.amplitude_show(nb)
    print("  Camino a la Impresora desde las PC:")
    for pc in ("Manjaro", "Red Hat", "Fedora"):
        camino(g2, pc, "Impresora")