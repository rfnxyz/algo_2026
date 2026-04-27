# FACTORIAL !
# factorial(5)  = 5 * 4 * 3 * 2 * 1
# 5!

# fac(5) = 5 * fac(4)
# fac(4) = 4 * fac(3)
# fac(3) = 3 * fac(2)
# fac(N) = N * fac(N-1) -> fac(0) = 1

# def factorial_r(num: int) -> int:
#     if num == 0:
#         return 1
#     else:
#         return num * factorial_r(num-1)
# 
# def factorial(num: int) -> int:
#     result = 1
#     for i in range(1, num + 1):
#         result = result * i
# 
#     return result

# print(factorial(5))
# print(factorial_r(5))

# fib(N) = fib(N-1) + fib(N-2) -> fib 0=0, fib 1=1

# fibonacci 
# def fibonacci_r(num: int) -> int:
#     if num == 0 or num == 1:
#         return num
#     else:
#         return fibonacci_r(num-1) + fibonacci_r(num-2)

##########  def fibonacci(num):
##########      fib_1 = 0
##########      fib_2 = 1
##########      for i in range(2, num+1):
##########          fib_aux = fib_1 + fib_2
##########          fib_1 = fib_2
##########          fib_2 = fib_aux
##########      
##########      return fib_aux
##########  print(fibonacci(150))
##########  print(fibonacci_r(50))

# 2)
# sum(n) = n + sum(n-1)         -> sum(0) = 0, sum(1) = 1

##########  def suma(num: int) -> int:
##########      if num == 0:
##########          return num
##########      else:
##########          return num+suma(num-1)
##########  print(suma(10))

# 3)
# 2*3 = 2+2+2 = 6
#prod(n,m) = n + prod(n,m-1)  ->  n,m = 0 -> 0

##########  def prod(n: int, m: int) -> int:
##########      if n==0 or m==0:
##########          return 0
##########      else:
##########          return n+prod(n,m-1)
##########  print(prod(4,4))

# 7)
# h(n) = 1/n + 1/n-1 + 1/n-2 ; n=1 -> 1

##########  def serie_h(num: int) -> float:
##########      if num == 1:
##########          return num
##########      else:
##########          return 1/num + serie_h(num-1)
##########  print(serie_h(4))

# 523 -> 52     5       -> n < 10 = 1
        # +1      +1

def count(num: int) -> int:
    if num <= 10:
        return 1
    else:
        return 1 + count(num // 10)

# print(count(5))
# print(count(52))
# print(count(523))
# print(count(5023))

# 4)
# pot(n,m) = m-1*(n*n)m=0 -> 1
# m=1 -> n
# n=0 -> 0
# m=-1 -> 1/n
# m<-1 -> 1/pot(n,m*-1)

##########  def pot(base: int, expo: int) -> float:
##########      res=base
##########      if base == 0:
##########          return 0
##########      elif expo == 0:
##########          return base
##########      elif expo == -1:
##########          return 1/base
##########  #    elif -1>expo:
##########  #        return 1/pot(base,expo*-1)
##########      else:
##########          for i in range(0, expo-1):
##########              res = res*base
##########          return res
##########  print(pot(5,3))

# 6)
# inverp(palab) = palabinv
# "hola" -> "aloh"
########## def inverp (palab: str) -> str:
##########     if palab == '':
##########         return palab
##########     else:
##########         return palab[::-1]
########## print(inverp("encefalogramaplano"))

# 7)
# nu = 5 -> 1/1 + 1/2 + 1/3 + 1/4 + 1/5
# nu -> 1/1 + 1/2 + 1/3 + ... + 1/nu
########## def serie1 (nu: float, nu2: float) -> float:
##########     for i in range(1, nu):
##########         nu2 = nu2 + 1/i
##########     return nu2
########## print(serie1(5,0))

# 8)
# decxbin(ndec) -> nbin
# ndec=2 -> 10
# ndec=4 -> 100
def decxbin(ndec: int) -> int:
    if ndec==0: return 0
    nbin = ""
    while ndec > 0:
        nbin = str(ndec % 2) + nbin
        ndec //= 2
    return nbin        
print(decxbin(35)) 

# 9)
# math.log(N / B, B) ->
import math
def logfrag(logB: float, logN: float) -> float:
    logX = math.log(logN, logB) + math.log(logB, logB)
    return logX
    return logB
    return logN
print(logfrag(10,43))
#print("log en base ", logB ," de ", logN ,"/", logB ," es igual a ",(logfrag(10,43)))

# 10)
# digint(num: int) -> int
# len(num) -> dig
# num = 5 -> dig = 1
# num = 10 -> dig = 2
# num = 100 -> dig = 3

def digint(numint: int) -> int:
    snum = str(numint)
    if numint < 0:
        return len(snum)-1
    else:
        return len(snum)
print(digint(-223))

# 11)

###########################################################################
###########################################################################
###########################################################################
###########################################################################
###########################################################################

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