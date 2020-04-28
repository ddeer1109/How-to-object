class Task:
    def __init__(self, id, name, state):
       self.id = id
       self.name = name
       self.state = state


class TaskService:
    def __init__(self, ile_taskow):
        """Inicjalizacja TaskService - tworzy listę obiektow TaskService.lista_taskow(ile_taskow)"""
        lista = []
        for i in range(ile_taskow):
            y = Task(i, "Obiekt " + str(i + 1), True)
            lista.append(y)
        self.lista_taskow = lista

    def __add__(self, obiekt):
        """Dodaj do TaskService.lista_taskow obiekt"""
        self.lista_taskow.append(obiekt)

    def __sub__(self, obiekt):
        """Usuń z TaskService.lista_taskow obiekt"""
        self.lista_taskow.remove(obiekt)

    def findByID(lista_taskow, id):
        """Zwraca z listy TaskService.lista_taskow obiekt Task o podanym id"""
        for i in range(len(lista_taskow)):
            if lista_taskow[i].id == id:
                return lista_taskow[i]

    def toggle(self, id):
        """zmienia state obiektu Task na liscie TaskService.lista_taskow na przeciwny"""
        TaskService.findByID(self.lista_taskow, id).state = not TaskService.findByID(self.lista_taskow, id).state

x = TaskService(7)
print("Find by ID " + str(TaskService.findByID(x.lista_taskow, 2)))
new = Task(23, "ALBERT", False)
print("new " + str(new))

print("")

x + new
print(x.lista_taskow[-1].id)
print(x.lista_taskow[-1].state)
x.toggle(x.lista_taskow[-1].id)
print(x.lista_taskow[-1].state)

print("")

print(x.lista_taskow)
x-new
print(x.lista_taskow)






