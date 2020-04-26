class Task:
    """Nowa klasa na potrzeby nauki"""
    def __init__(self, id, name, state):
       self.id = id
       self.name = name
       self.state = state

    def __add__(self, skl):
        return Task(self.id + skl, self.name, self.state)

    def __sub__(self, skl):
        return Task(self.id - skl, self.name, self.state)

    def lista_obiektow(ile):
        lista = []
        for i in range(ile):
            y = str(i + 1)
            y = Task(i, "Obiekt " + str(i + 1), True)
            lista.append(y)
        return lista

    def findByID(lista, id):
        for i in range(len(lista)):
            if lista[i].id == id:
                return lista[i]
            else:
                print("Brak obiektu o takim ID")

    def toggle(self):
        if self.state == True:
            self.state = False
        elif self.state == False:
            self.state = True


x = Task.lista_obiektow(ile=5)

f = Task.findByID(x, 0)
print(f)
print(f.id, f.name, f.state)

f = f + 1
print(f.id, f.name, f.state)

f = f-10
print(f.id, f.name, f.state)

Task.toggle(f)
print(f.id, f.name, f.state)








