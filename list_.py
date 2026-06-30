from typing import Any, Optional

class List(list):               # SELF es list (la lista con los elementos)
    
    __CRITERION_FUNCTION = {}   # Definir criterio en función en clase, diccionario vacío

    # Almacenar en función
    def add_criterion(self, criterion_key: str, criterion_function) -> None:
        self.__CRITERION_FUNCTION[criterion_key] = criterion_function


    def show(self) -> None:     # Mostrar lista
        for element in self:
            print(element)
    
    def search(self, search_value: Any):    # Método búsqueda, chequear si existe
        # Tener en cuenta que la lista debe estar ordenada
        self.sort_by_criterion(key_criterion=criterion)
        search_criterion = self.__CRITERION_FUNCTION.get(criterion)

        # --------------- BÚSQUEDA BINARIA

        start = 0
        end = len(self) -1
        middle = (start + end) // 2

        while start <= end:
#             value = self[middle]

            if search_criterion is None and not isinstance(self[0], (bool, int, float, str)):
                print('no se pudo determinar criterio de busqueda')
                return None

            value = search_criterion(self[middle]) if search_criterion else self[middle]

            if value.nom == search_value:   # Si el buscado es el medio o distinto
                return middle
            elif value.nom < search_value:
                start = middle + 1
            else:
                end = middle -1
            
            middle = (start + end) // 2

    # Insertar: Mantendremos el APPEND o el INSERT puede definir un INSERT_VALUE si lo desean

    def delete_value(self, value, criterion=None) -> Optional[Any]:     # Eliminar
        index = self.search(value, criterion)

        return self.pop(index) if index is not None else None

    def sort_by_criterion(self, key_criterion=None) -> None:        # Ordenar por criterio X

        sort_criterion = self.__CRITERION_FUNCTION.get(key_criterion)

        if sort_criterion:                                  # Por dato primitivo o compuesto
            self.sort(key=sort_criterion)
        elif self and isinstance(self[0], (bool, int, float, str)):
            self.sort()
        else:
            print('no se puede ordenar la lista no se como se debe ordenar')

    def size(self) -> int:      # Longitud
        return len(self)

    def filter_contain_on_bio(self, values):
        for element in self:
            if any(value in element.bio.lower() for value in values):
                print(element)

    def filter_start_with(self, values):
        for element in self:
            if element.name.startswith(values):
                print(element)


# l = List()

# l.append(1)
# l.append(3)
# l.append(5)
# l.append(7)

# print(l.search(5))
# print(l.search(17))


# class Persona:
# 
#     def __init__(self, nom, ape, edad):               # Constructor
#         self.nom = nom
#         self.ape = ape
#         self.edad = edad
# 
#     def __str__(self):                                # Método STR para hacer print
#         return f"{self.ape} {self.nom} {self.edad}"
# 
# 
# l.append(Persona("Ana", "Blanc", 42))
# l.append(Persona("Dario", "Aron", 12))
# l.append(Persona("Juan", "Perez", 24))

### def by_name(item):
###     return item.nom

### def by_last_name(item):
###     return item.ape

### def by_age(item):
###     return item.edad


### l.sort(key=by_age)  # Parámetro KEY necesita función, cuando llega objeto, se devuelve un dato útil para el método
                        # (funciona con primitivos)

# print(l.search("Dario"))

# l.show()

# Para cualquier función de ordenamiento, para ordenar elemento se necesita comparar
# No se puede comparar objeto porque son dos direcciones de memoria (dos iguales o dos distintos)
# Al pedir comparar dos objetos, SORT verifica si son el mismo tipo de dato y si son primitivos
# SORT llama a la función y se refiere a KEY