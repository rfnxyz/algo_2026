from copy import copy, deepcopy
from typing import Any
# Deepcopy : Copia "profunda" rompe enlace/función recursiva/que las vdos variables vayam al mismo lugar

class Stack:
###     elements = []                           # Lista
    # Doble guión bajo (__) para privacidad, nadie fuera de la clase puede modificar
        # Método CONSTRUCTOR, inicializador de la clase y atributos, creador de objetos
            # Crear estructura -> asignar valores por defecto en el constructor
            # Objeto/atributo suele (debería) tener valor
            # Constructor no definido : Clase siempre hereda de OBJECT por defecto
                # SELF : representa el objeto que la clase va a llamar
                    # def : MÉTODO
    def __init__(self):                     # Lista, 'Constructor'
        self.__elements = []
        
    def push(self, value: Any) -> None:     # MÉTODO 'Apilar'
        self.__elements.append(value)       # Append a lista Elements.
        # APPEND en vez de INSERT porque va a ir siempre la última posición del arreglo

    def pop(self) -> Any:                   # Desapilar de lista
        return self.__elements.pop()
    
    def show(self) -> None:                 # Mostrar, no válida en todos los lenuajes, apropiada en Python
###        print(self.__elements)
        stack_aux = Stack()                 # Auxiliar
        stack_aux.__elements = copy(self.__elements)

        while stack_aux.size() > 0: 
            value = stack_aux.pop()
            print(value)
        
###        stack_aux = Stack()              # Mostrar, solución "estándar" para todos los lenguajes

###        while self.size() > 0:           # Se utiliza estructura de datos 
###            value = self.pop()
###            print(value)
###            stack_aux.push(value)
###        
###        while stack_aux.size() > 0: 
###            value = stack_aux.pop()
###            self.push(value)
        
    def size(self) -> int:                  # Devolver tamaño pila
        return len(self.__elements)
    
    def on_top(self) -> Any:                # Devolver objeto en pila sin quitarlo
        if self.size() > 0:
            return self.__elements[-1]

#f_1 = Stack()                      
#f_1.name = "Ricardo"               

#pila = Stack()
#
#pila.push(1)                               # Poner número
#pila.show()
#### print(pila.elements)
#
#pila.push(2)
#pila.show()
#### print(pila.elements)
#
#pila.elements.clear()
#
#pila.push(3)
#pila.show()
#pila.pop()
#### print(pila.elements)
#
#pila.push(4)
#pila.show()
#### print(pila.elements)