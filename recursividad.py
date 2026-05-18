#FACTORIAL !
#factorial(5)  = 5 * 4 * 3 * 2 * 1
#5!

#fac(5) = 5 * fac(4)
#fac(4) = 4 * fac(3)
#fac(3) = 3 * fac(2)
#fac(N) = N * fac(N-1) -> fac(0) = 1

#def factorial_r(num: int) -> int:
#    if num == 0:
#        return 1
#    else:
#        return num * factorial_r(num-1)
#
#def factorial(num: int) -> int:
#    result = 1
#    for i in range(1, num + 1):
#        result = result * i
#
#    return result

#print(factorial(5))
#print(factorial_r(5))

#fib(N) = fib(N-1) + fib(N-2) -> fib 0=0, fib 1=1

#fibonacci 
#def fibonacci_r(num: int) -> int:
#    if num == 0 or num == 1:
#        return num
#    else:
#        return fibonacci_r(num-1) + fibonacci_r(num-2)

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

#print(count(5))
#print(count(52))
#print(count(523))
#print(count(5023))

# 4)
# pot(n,m) = m-1*(n*n)m=0 -> 1
# m=1 -> n
# n=0 -> 0
# m=-1 -> 1/n
# m<-1 -> 1/pot(n,m*-1)

########## def pot(base: int, expo: int) -> float:
##########     res=base
##########     if base == 0:
##########         return 0
##########     elif expo == 0:
##########         return base
##########     elif expo == -1:
##########         return 1/base
########## #    elif -1>expo:
########## #        return 1/pot(base,expo*-1)
##########     else:
##########         for i in range(0, expo-1):
##########             res = res*base
##########         return res
########## print(pot(5,3))

# 6)
# inverp(palab) = palabinv
# "hola" -> "aloh"

##########def inverp (palab: str) -> str:
##########    if palab == '':
##########        return palab
##########    else:
##########        return palab[::-1]
##########print(inverp("encefalogramaplano"))

# 7)
# nu = 5 -> 1/1 + 1/2 + 1/3 + 1/4 + 1/5
# nu -> 1/1 + 1/2 + 1/3 + ... + 1/nu

##########def serie1 (nu: float, nu2: float) -> float:
##########    for i in range(1, nu):
##########        nu2 = nu2 + 1/i
##########    return nu2
##########print(serie1(5,0))

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