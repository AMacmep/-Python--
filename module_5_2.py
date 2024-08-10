# Домашняя работа по уроку "Специальные методы классов"
class House():
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        for flor in range(new_floor):
            if new_floor > self.number_of_floors or new_floor < 1:
                print('Такого этажа не существует')
                break
            else:
                print(flor+1)
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return "Название: " + self.name + " , кол-во этажей: " + str(self.number_of_floors)



h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))