from random import randint
from stack import Stack


# 1)
# Determinar el núm. de ocurrencias de un determinado elemento en una pila

### pila = Stack()
### 
### for i in range(10):
###     pila.push(randint(1, 10))
### 
### print()
### pila.show()
### print()
### 
### search_value = int(input('Ingrese un número para contar ocurrencias '))
### counter = 0
### 
### while pila.size() > 0:
###     value = pila.pop()
###     if value == search_value:
###         counter += 1
###    
### print(f'Cantidad de ocurrencias de {search_value} en la pila: {counter}')

# 2)
# Eliminar de una pila todos los elem. impares. Que en la misma solo queden números pares.

pila = Stack()

for i in range(10):
    pila.push(randint(1, 10))

pila_aux = Stack()

while pila.size() > 0:
    value = pila.pop()              # Sacar valor en la cima
    if value % 2 == 0:
        pila_aux.push(value)

while pila_aux.size() > 0:
    value = pila_aux.pop()
    pila.push(value)

pila.show()
print()
pila.show()
print()