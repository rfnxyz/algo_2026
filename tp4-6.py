from list_ import List

# Clase 
class Superhero:
    def __init__(self, nombre, anio, casa, bio):
        self.name = nombre
        self.year = anio
        self.house = casa
        self.bio = bio

    def __str__(self):
        return (f"Nombre: {self.name} - Año: {self.year} - Casa: {self.house} - Bio: {self.bio}")

# Funciones criterio
def by_name(item):
    return item.name

def by_year(item):
    return item.year

# Datos
datos = [
    ("Spider-Man",        1962, "Marvel", "Peter Parker viste un traje rojo y azul con poderes arácnidos."),
    ("Iron Man",          1963, "Marvel", "Tony Stark construyó una armadura de alta tecnología para escapar de sus captores."),
    ("Wolverine",         1974, "Marvel", "Logan posee garras de adamantium y regeneración acelerada. Miembro de los X-Men."),
    ("Batman",            1939, "DC",     "Bruce Wayne combate el crimen usando una armadura táctica y tecnología avanzada."),
    ("Superman",          1938, "DC",     "Kal-El fue enviado desde Krypton. Defiende la Tierra con poderes solares."),
    ("Mujer Maravilla",   1941, "DC",     "Diana, princesa amazona, porta el lazo de la verdad y brazaletes indestructibles."),
    ("The Flash",         1956, "DC",     "Barry Allen se mueve a velocidades superlumínicas conectado a la Fuerza de la Velocidad."),
    ("Linterna Verde",    1959, "DC",     "Hal Jordan usa un anillo que materializa construcciones de energía verde."),
    ("Dr. Strange",       1963, "Marvel", "Hechicero supremo que protege la Tierra de amenazas místicas."),
    ("Capitana Marvel",   1968, "Marvel", "Carol Danvers, ex piloto con poderes cósmicos."),
    ("Black Panther",     1966, "Marvel", "Rey de Wakanda que viste un traje de vibranium indestructible."),
    ("Star-Lord",         1976, "Marvel", "Peter Quill, líder de los Guardianes de la Galaxia."),
    ("Shazam",            1939, "DC",     "Billy Batson se convierte en héroe al pronunciar una palabra mágica."),
    ("Martian Manhunter", 1955, "DC",     "J'onn J'onzz, el último marciano, con poderes telepáticos y de metamorfosis."),
    ("Black Widow",       1964, "Marvel", "Natasha Romanoff, espía de élite entrenada en el programa Habitación Roja."),
]

lista_heroes = List()
lista_heroes.add_criterion('name', by_name)
lista_heroes.add_criterion('year', by_year)

for d in datos:
    lista_heroes.append(Superhero(d[0], d[1], d[2], d[3]))

# 6a eliminar linterna verde
eliminado = lista_heroes.delete_value("Linterna Verde", 'name')
if eliminado:
    print(f"Eliminado: {eliminado.name}")
else:
    print("No se encontró Linterna Verde.")

# 6b año wolverine
idx = lista_heroes.search("Wolverine", 'name')
if idx is not None:
    print(f"Wolverine apareció en {lista_heroes[idx].year}.")
else:
    print("No se encontró Wolverine.")

# 6c cambiar casa de dr. strange
idx = lista_heroes.search("Dr. Strange", 'name')
if idx is not None:
    lista_heroes[idx].house = "DC"
    print(f"Dr. Strange ahora pertenece a DC.")
else:
    print("No se encontró Dr. Strange.")


# 6d mencion "traje", "armadura"
lista_heroes.filter_contain_on_bio(['traje', 'armadura'])

# 6e 1963
for heroe in lista_heroes:
    if heroe.year < 1963:
        print(f"{heroe.name} - {heroe.house}")

# 6f casa cap marvel y wonder
for nombre in ["Capitana Marvel", "Mujer Maravilla"]:
    idx = lista_heroes.search(nombre, 'name')
    if idx is not None:
        print(f"{nombre}: {lista_heroes[idx].house}")
    else:
        print(f"No se encontró {nombre}.")

# 6g info flash starlord
for nombre in ["The Flash", "Star-Lord"]:
    idx = lista_heroes.search(nombre, 'name')
    if idx is not None:
        print(f"{lista_heroes[idx]}")
    else:
        print(f"No se encontró {nombre}.")

# 6h b m s
lista_heroes.filter_start_with(('B', 'M', 'S'))

# 6i heroes por casa
conteo = {}
for heroe in lista_heroes:
    conteo[heroe.house] = conteo.get(heroe.house, 0) + 1
for casa, cantidad in conteo.items():
    print(f"{casa}: {cantidad} superhéroe(s)")