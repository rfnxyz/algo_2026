# 5)
# roman(nr) = abc
# numlist = [5, 4, 1]
# romlist = ["V", "IV", "I"]
# nr = 1 -> I
# nr = 4 -> IV
# nr = 5 -> V
# def roman(numrom: input(string))

def roman(nr: int):
    valo = [1000000, 900000, 500000, 400000, 100000, 90000, 50000, 40000, 10000, 9000 ,5000, 4000, 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    simb = ["M_", "DM_", "D_", "ID_", "C_", "IC_", "L_", "IL_", "X_", "IX_", "V_", "IV_", "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    # La terminal no representa los vinculum (sobrerayado sobre el símbolo) en los valores a partir del 4000 en adelante, para sortear este problema, dichos símbolos presentan un guión bajo posterior. 
    nr2 = float(nr)
    nurrom = ''
    for i in range(len(valo)):
        while nr >= valo[i]:
            nurrom += (simb[i])
            nr -= valo[i]
    return nurrom
print(roman(1888888))

###########################################################################
###########################################################################
###########################################################################
###########################################################################
###########################################################################

# 22)
# def fuerza
# list = [sable, obj1, obj2, obj3, obj4, obj5, ...]
# fuerza() -> obj1 =! sable -> found: negativo, reintentos = x+1, lista = x-1
# fuerza() -> sable -> found: positivo, detener búsqueda

import random
def usar_la_fuerza(mochi, objs = 0):
    print("Usted es"'\u001b[34m'" Lucas caminante del cielo "'\u001b[0m'"y necesitás encontrar el"'\u001b[34m'" palito de luz "'\u001b[0m'"presuntamente ubicado dentro de tu"'\u001b[34m'" mochila "'\u001b[0m'",necesita aplicar"'\u001b[34m'" fuerza "'\u001b[0m'"para sacar un objeto de la mochila.")
    input("Presione cualquier tecla para aplicar fuerza...")
    cantidad = int(len(mochi))
    # Mochila vacía
    if len(mochi) == 0:
        print("La mochila está vacía, Lucas caminante del cielo es boleta.")
        return False, objs
    # Mochila con ítems dentro
    else:
        print("Hay",'\u001b[33m'+ str(cantidad) +'\u001b[0m',"objetos dentro de la mochila.")
        if "sable de luz" in mochi:
            print('\u001b[34m'"Se sabe que el palito de luz está en la mochila, solo falta encontrarlo."'\u001b[0m')
        input("Presione cualquier tecla para aplicar fuerza...")
        for j in range(0, cantidad):
            #idx = random.randrange(mochi)
            objx = random.choice(mochi)
            #objx = str(mochi[idx])
            #mochi = mochi[:idx] + mochi[idx+1]
            if objx == 'sable de luz':
                objs += 1
                print('\u001b[32m'"Se encontró el palito de luz, tras",'\u001b[33m'+ str(objs) +'\u001b[0m','\u001b[32m'"intentos de aplicar fuerza."'\u001b[0m')
                return True, objs
            else:
                print("Se encontró:",'\u001b[33m'+ str(objx) +'\u001b[0m',". Claramente no es el palito de luz.",'\u001b[33m'+ str(len(mochila)-1) +'\u001b[0m',"objetos restantes.")
                #mochi.pop(idx)
                mochi.remove(objx)
                objs += 1
                if len(mochi) == 0:
                    print('\u001b[31m',"No se encontró el palito de luz, Lucas el caminante del cielo es boleta."'\u001b[0m')
                    return False, objs
            input("Presione cualquier tecla para aplicar fuerza...")

mochila = [
    "raciones",
    "botella de agua",
    "puñado de arena",
    "pelusa de bolsillo",
    "CD con 'grandes éxitos' de Nickelback",
    "Samsung Galaxy J2 Prime con la pantalla quebrada",
    "moneda de 25 centavos argentinos",
    "billete de 50 australes argentinos",
    "mota",
    "conveniencia de guión",
#    "sable de luz",
]
print(usar_la_fuerza(mochila))