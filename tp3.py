from queue_ import Queue
from stack import Stack

# 10

# # notif = [(hora, aplicación, mensaje)]
# notificaciones = [
#     ("10:15", "Instagram", "Tu publicación obtuvo 10 likes."),
#     ("11:43", "Facebook", "Juan te etiquetó en una foto."),
#     ("12:05", "Twitter", "Nuevo seguidor: @pythondev."),
#     ("12:30", "Facebook", "María comentó tu publicación."),
#     ("13:10", "Twitter", "Tendencia: Python supera a Java en popularidad."),
#     ("14:22", "WhatsApp", "Mensaje de grupo: Algoritmos 2026."),
#     ("15:00", "Facebook", "Recordatorio: evento mañana."),
#     ("15:57", "Twitter", "Python 4.0 fue anunciado oficialmente."),
#     ("16:30", "Instagram", "Nueva historia de @usuario."),
#     ("17:10", "Twitter", "Hilo interesante sobre estructuras de datos."),
# ]
# 
# cola_notif = Queue()
# for n in notificaciones:
#     cola_notif.arrive(n)
# 
# # Retorna lista con todos los elementos de principio a fin
# def recorrer_cola(cola):
#     elementos = []
#     for _ in range(cola.size()):
#         valor = cola.move_to_end()
#         elementos.append(valor)
#     return elementos
# 
# # Eliminar notificaciones de Facebook
# def eliminar_facebook(cola):
#     print("=== A) Eliminando notificaciones de Facebook ===")
#     eliminadas = 0
#     aux = Queue()
# 
#     while cola.size() > 0:
#         notif = cola.attention()
#         hora, app, mensaje = notif
#         if app == "Facebook":
#             print(f"  Eliminada: [{hora}] {mensaje}")
#             eliminadas += 1
#         else:
#             aux.arrive(notif)
# 
#     # Restaurar la cola sin los de Facebook
#     while aux.size() > 0:
#         cola.arrive(aux.attention())
# 
#     print(f"  Total eliminadas: {eliminadas}")
# 
# # Notificaciones de Twitter con la palabra 'Python'
# def twitter_con_python(cola):
#     print("=== B) Notificaciones de Twitter con 'Python' ===")
#     elementos = recorrer_cola(cola)
#     encontradas = 0
# 
#     for hora, app, mensaje in elementos:
#         if app == "Twitter" and "Python" in mensaje:
#             print(f"  [{hora}] {mensaje}")
#             encontradas += 1
# 
#     if encontradas == 0:
#         print("  No hay notificaciones de Twitter con la palabra 'Python'.")
# 
# # Notificaciones en un rango horario
# def notif_en_rango_con_pila(cola, hora_inicio, hora_fin):
#     print(f"=== C) Notificaciones entre {hora_inicio} y {hora_fin} ===")
#     elementos = recorrer_cola(cola)
#     pila_rango = Stack()
# 
#     for hora, app, mensaje in elementos:
#         if hora_inicio <= hora <= hora_fin:
#             pila_rango.push((hora, app, mensaje))
# 
#     cantidad = pila_rango.size()
#     print(f"  Notificaciones en el rango (almacenadas en pila): {cantidad}")
# 
#     # Mostrar el contenido de la pila
#     while pila_rango.size() > 0:
#         hora, app, mensaje = pila_rango.pop()
#         print(f"  [{hora}] {app}: {mensaje}")
# 
# eliminar_facebook(cola_notif)
# twitter_con_python(cola_notif)
# notif_en_rango_con_pila(cola_notif, "11:43", "15:57")

# 22

# Cada personaje es una tupla (nombre_personaje, superheroe, genero)
personajes = [
    ("Tony Stark",          "Iron Man",             "M"),
    ("Steve Rogers",        "Capitán América",      "M"),
    ("Natasha Romanoff",    "Black Widow",          "F"),
    ("Thor Odinson",        "Thor",                 "M"),
    ("Bruce Banner",        "Hulk",                 "M"),
    ("Carol Danvers",       "Capitana Marvel",      "F"),
    ("Scott Lang",          "Ant-Man",              "M"),
    ("Wanda Maximoff",      "Scarlet Witch",        "F"),
    ("Peter Parker",        "Spider-Man",           "M"),
    ("Shuri",               "Black Panther",        "F"),
    ("Sam Wilson",          "Capitán América",      "M"),
    ("Stephen Strange",     "Doctor Strange",       "M"),
    ("Yelena Belova",       "Black Widow",          "F"),
    ("Hope Van Dyne",       "Wasp",                 "F"),
    ("Peter Quill",         "Star-Lord",            "M"),
]

cola_mcu = Queue()
for p in personajes:
    cola_mcu.arrive(p)

def recorrer_cola(cola):
    """
    Recorre la cola usando una pila como auxiliar.
    Retorna una lista con los elementos en orden (frente → fondo).
    """
    pila_aux = Stack()
    elementos = []

    # Desencolar todo hacia la pila
    while cola.size() > 0:
        item = cola.attention()
        elementos.append(item)
        pila_aux.push(item)

    # Restaurar la cola desde la pila (el orden se invierte dos veces, queda igual)
    cola_aux = Queue()
    while pila_aux.size() > 0:
        cola_aux.arrive(pila_aux.pop())

    while cola_aux.size() > 0:
        cola.arrive(cola_aux.attention())

    return elementos

def buscar_personaje_por_heroe(cola, nombre_heroe):
    print(f"\n=== A) Personaje de {nombre_heroe} ===")
    elementos = recorrer_cola(cola)

    for nombre, heroe, genero in elementos:
        if heroe == nombre_heroe:
            print(f"  {nombre_heroe} es interpretado por el personaje: {nombre}")
            return

    print(f"  No se encontró el superhéroe '{nombre_heroe}' en la cola.")

def heroes_femeninos(cola):
    print("\n=== B) Superhéroes femeninos ===")
    elementos = recorrer_cola(cola)
    encontrado = False

    for nombre, heroe, genero in elementos:
        if genero == "F":
            print(f"  {heroe}")
            encontrado = True

    if not encontrado:
        print("  No hay superhéroes femeninos en la cola.")

def personajes_masculinos(cola):
    print("\n=== C) Personajes masculinos ===")
    elementos = recorrer_cola(cola)
    encontrado = False

    for nombre, heroe, genero in elementos:
        if genero == "M":
            print(f"  {nombre}")
            encontrado = True

    if not encontrado:
        print("  No hay personajes masculinos en la cola.")

def buscar_heroe_por_personaje(cola, nombre_personaje):
    print(f"\n=== D) Superhéroe de {nombre_personaje} ===")
    elementos = recorrer_cola(cola)

    for nombre, heroe, genero in elementos:
        if nombre == nombre_personaje:
            print(f"  {nombre_personaje} es el superhéroe: {heroe}")
            return

    print(f"  No se encontró el personaje '{nombre_personaje}' en la cola.")

def buscar_heroe_por_personaje(cola, nombre_personaje):
    print(f"\n=== D) Superhéroe de {nombre_personaje} ===")
    elementos = recorrer_cola(cola)

    for nombre, heroe, genero in elementos:
        if nombre == nombre_personaje:
            print(f"  {nombre_personaje} es el superhéroe: {heroe}")
            return

    print(f"  No se encontró el personaje '{nombre_personaje}' en la cola.")

def buscar_carol_danvers(cola):
    print("\n=== F) ¿Carol Danvers está en la cola? ===")
    elementos = recorrer_cola(cola)

    for nombre, heroe, genero in elementos:
        if nombre == "Carol Danvers":
            print(f"  Sí, Carol Danvers está en la cola. Su superhéroe es: {heroe}")
            return

    print("  Carol Danvers no se encuentra en la cola.")

buscar_personaje_por_heroe(cola_mcu, "Capitana Marvel")
heroes_femeninos(cola_mcu)
personajes_masculinos(cola_mcu)
buscar_heroe_por_personaje(cola_mcu, "Scott Lang")
filtrar_por_inicial_s(cola_mcu)
buscar_carol_danvers(cola_mcu)