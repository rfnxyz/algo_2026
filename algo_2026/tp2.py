# pila
from stack import Stack

# 20)
# movimiento = N -> retorno = S (opuesto de movimiento)
# lista movimiento: S ; E ; W ; NE ; NW ; SE ; SW
# lista retorno:    N ; E ; E ; SW ; SE ; NW ; NE

###opuestos = {    # Direcciones y sus opuestos
###    "N":    "S",
###    "S":    "N",
###    "E":    "W",
###    "W":    "E",
###    "NE":   "SW",
###    "NW":   "SE",
###    "SE":   "NW",
###    "SW":   "NE",
###}
###
###direcciones = list(opuestos.keys())
###
###def reg_mov():          # Registro
###    pila1 = Stack()
###
###    print(" - Registro de movimientos del robot -") 
###    print("Direcciones válidas:")
###    print("NW  N  NE")
###    print(". ↖ ↑ ↗ .")
###    print("W ← @ → E")
###    print(". ↙ ↓ ↘ .")
###    print("SW  S  SE")
###    print("Escriba 'fin' para terminar el registro")
###
###    while True:
###        direc = input('\u001b[34m'"Dirección\u001b[0m: ")
###
###        if direc == "fin":
###            break
###
###        if direc not in direcciones:
###            print("'\u001b[31m'Dirección'\u001b[0m' inválida. Intente de nuevo")
###            continue
###        
###        try:
###            pasos = int(input("Cantidad de\u001b[34m pasos\u001b[0m en esa dirección: "))
###            if pasos <=0:
###                print("Ingrese un número\u001b[31m mayor a cero\u001b[0m.")
###                continue
###        except ValueError:
###            print("Debe ingresar un\u001b[31m número válido\u001b[0m.")
###            continue
###        
###        movimiento = (pasos, direc)
###        pila1.push(movimiento)
###        print("Movimiento registrado. \u001b[34m",pasos,"\u001b[0m paso(s) en dirección \u001b[34m",direc,"\u001b[0m.")
###
###    return pila1
###
###def retorno(pila1):     # Retorno, invertir direcciones de pila
###    pasos_retorno = int()
###    if pila1.size() == 0:
###        print("No hay movimientos registrados.\u001b[31m El robot no se movió."'\u001b[0m')
###        return
###    
###    while pila1.size() != 0:
###        pasos_retorno += 1
###        pasos, direc = pila1.pop()
###        direc_vuelta = opuestos[direc]
###        print("Paso nro.\u001b[35m",pasos_retorno,"\u001b[0m : \u001b[35m",pasos,"\u001b[0m paso(s) en dirección \u001b[35m",direc_vuelta,"\u001b[0m.")    
###    print('\u001b[32m'"El robot ha regresado al punto de partida."'\u001b[0m')
###
###pila_mov = reg_mov()
###print("Movimientos registrados: \u001b[35m",pila_mov.size(),"\u001b[0m.")
###retorno(pila_mov)

# 24)
pjs = [         #pjs = [(nombre,apariciones)]
    ("Thor",8),
    ("Rocket Raccoon",7),
    ("Iron Man",10),
    ("Groot",5),
    ("Viuda Nergra",7),
    ("Capitán América",6),
    ("Doctor Strange",5),
    ("Gamora",6),
    ("Hawkeye",4),
    ("Capitana Marvel",4),
    ("Orax",5),
    ("Cull Obsidian",5),
]
pila_mcu = Stack()

for i in pjs:
    pila_mcu.push(i)

def recorrer(pila2):
    pila_aux = Stack()
    elements = []

    while pila2.size() > 0:
        item = pila2.pop()
        elements.append(item)
        pila_aux.push(item)
    
    while pila_aux.size() > 0:
        pila2.push(pila_aux.pop())
    
    return elements

def busqueda(pila2, buscados):
    print("- Posición de pesonajes -")
    elements = recorrer(pila2)
    encontrados = 0

    for i, (nombre, apariciones) in enumerate(elements):
        if nombre in buscados:
            print(f"{nombre}: Posición {i+1} desde la cima")
            encontrados += 1
        if encontrados == len(buscados):
            break

    if encontrados == 0:
        print("No se encontró ninguno de los personajes buscados.")

def mas5apariciones(pila2):
    print("- Personajes con más de 5 películas -")
    elements = recorrer(pila2)
    found = False

    for nombre, apariciones in elements:
        if apariciones > 5:
            print(f"{nombre} posee {apariciones} apariciones.")
            found = True
    
    if not found:
        print("Ningún personaje aparece en más de 5 películas.")

def apariciones_viuda_negra(pila2):
    print("- Apariciones Viuda Negra -")
    elements = recorrer(pila2)

    for nombre, apariciones in elements:
        if nombre == "Viuda Negra":
            print(f"Viuda Negra aparece en {apariciones} películas.")
            return
    print("Viuda Negra no está en la pila.")

def filtrar_x_inicial(pila2, inicial):
    print(f"- Personajes cuyo nombre empieza con {inicial}")
    elements = recorrer(pila2)
    found = False

    for nombre, apariciones in elements:
        if nombre[0].upper() in [l.upper()for l in inicial]:
            print(f"{nombre} ({apariciones} películas).")
            found = True
    if not found:
        print("No hay personajes con esa(s) inicial(es).")

busqueda(pila_mcu, ["Rocket Raccoon","Groot"])
mas5apariciones(pila_mcu)
apariciones_viuda_negra(pila_mcu)
filtrar_x_inicial(pila_mcu,["C","D","G"])