from copy import copy, deepcopy
from typing import Any

class Stack:
###     elements = []                           # Lista
    
    # Doble guión bajo (__) para privacidad, nadie fuera de la clase puede modificar
        # Método constructor, inicializador de la clase
            # self, representa el objeto que la clase va a llamar
    def __init__(self):                         # Lista
        self.__elements = []
        
    def push(self, value: Any) -> None:         # Método 'Apilar'
        self.__elements.append(value)           # Append a lista Elements.
        # Append en vez de Insert porque va a ir siempre la última posición del arreglo

    def pop(self) -> Any:                       # Desapilar de lista
        return self.__elements.pop()
    
    def show(self) -> None:                     # Mostrar
###        print(self.__elements)
        stack_aux = Stack()
        stack_aux.__elements = copy(self.__elements)

        while stack_aux.size() > 0: 
            value = stack_aux.pop()
            print(value)
        
###        stack_aux = Stack()

###        while self.size() > 0: 
###            value = self.pop()
###            print(value)
###            stack_aux.push(value)
###        
###        while stack_aux.size() > 0: 
###            value = stack_aux.pop()
###            self.push(value)
        
    def size(self) -> int:                      # Devolver tamaño pila
        return len(self.__elements)
    
    def on_top(self) -> Any:                    # Devolver objeto en pila sin quitarlo
        if self.size() > 0:
            return self.__elements[-1]

#pila = Stack()
#
#pila.push(1)                                    # Poner número
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