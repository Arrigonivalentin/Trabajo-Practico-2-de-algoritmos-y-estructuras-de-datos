# Se tienen dos pilas con personajes de Star Wars, en una los del episodio V de “The empire
# strikes back” y la otra los del episodio VII “The force awakens”. Desarrollar un algoritmo que
# permita obtener la intersección de ambas pilas, es decir los personajes que aparecen en ambos episodios.

class Stack:

        def __init__(self):
            self.elements =[]

        def push(self,element):
            self.elements.append(element)

        def pop(self):
            if len(self.elements) > 0:
                return self.elements.pop()
            else:
                return None

        def on_top(self):
            if len(self.elements) > 0:
                return self.elements[-1]
            else:
                return None

        def size(self):
            return len(self.elements)


pila_epiV = Stack()
pila_epiVII = Stack()
pila_iguales = Stack()
pila_aux2 = Stack()

nombres_epiV=["Luke Skywalker","Darth Vader","Han Solo"]
nombres_epiVII=["Finn","Luke Skywalker","Rey"]

for element in nombres_epiV:
    pila_epiV.push(element)

for element2 in nombres_epiVII:
    pila_epiVII.push(element2)

def interseccion_pilas(pila_epiV, pila_epiVII):
    return list(set(pila_epiV.elements) & set(pila_epiVII.elements))

print(interseccion_pilas(pila_epiV,pila_epiVII))