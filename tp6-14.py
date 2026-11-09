# 14
from graph import Graph

AMBIENTES = [
    "cocina", "comedor", "cochera", "quincho", "baño 1", "baño 2",
    "habitación 1", "habitación 2", "sala de estar", "terraza", "patio",
]

# (ambiente A, ambiente B, distancia en metros)  -- distancias supuestas
CONEXIONES = [
    ("cocina", "comedor", 4), ("cocina", "patio", 8), ("cocina", "baño 1", 6),
    ("cocina", "sala de estar", 7), ("cocina", "cochera", 9),
    ("comedor", "sala de estar", 5), ("comedor", "patio", 6),
    ("cochera", "quincho", 7), ("cochera", "patio", 11),
    ("quincho", "terraza", 9), ("quincho", "baño 2", 10),
    ("baño 1", "habitación 1", 3), ("baño 1", "habitación 2", 5),
    ("baño 2", "habitación 2", 2), ("baño 2", "terraza", 6), ("baño 2", "patio", 7),
    ("habitación 1", "sala de estar", 4), ("habitación 1", "habitación 2", 4),
    ("habitación 2", "sala de estar", 6), ("terraza", "sala de estar", 6),
]

def cargar():
    g = Graph(is_dir=False)
    for ambiente in AMBIENTES:
        g.add_vertex(ambiente)
    for a, b, metros in CONEXIONES:
        g.add_edge(metros, a, b)
    return g

if __name__ == "__main__":
    g = cargar()

    print("=== b) Aristas por ambiente ===")
    for v in g:
        print(f"  {v.value}: {len(v.edges)} aristas")

    print("\n=== c) Árbol de expansión mínimo (cables) ===")
    aristas, total = g.prim("cocina")
    for padre, hijo, metros in aristas:
        print(f"  {padre} -- {hijo}: {metros} m")
    print(f"  Total de cable: {total} metros")

    print("\n=== d) Camino más corto: habitación 1 -> sala de estar ===")
    ruta, costo = g.camino_mas_corto("habitación 1", "sala de estar")
    print(f"  {' -> '.join(ruta)}: {costo} metros")
    ruta, costo = g.camino_mas_corto("habitación 2", "sala de estar")
    print(f"  (desde habitación 2) {' -> '.join(ruta)}: {costo} metros")
