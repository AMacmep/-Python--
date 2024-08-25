#Домашнее задание по теме "Зачем нужно наследование"
class Animal:
    alive = True #Живой
    fed = False #Голодный
    def __init__(self, name):
        self.name = name

class Plant:
    edible = False # несъедобный
    def __init__(self, name):
        self.name = name
class Mammal(Animal):
    def eat(self, food):
        if food.edible: # Если еда съедобная
            self.fed = True # то животное насытилось
            print(f'{self.name} съел {food.name}')
        else:
            self.alive = False # Иначе, животное погибает
            print(f'{self.name} не стал есть {food.name}')
class Predator(Animal):
    def eat(self, food):
        if food.edible:  # Если еда съедобная
            self.fed = True  # то животное насытилось
            print(f'{self.name} съел {food.name}')
        else:
            self.alive = False  # Иначе, животное погибает
            print(f'{self.name} не стал есть {food.name}')
class Flower(Plant):
    def __init__(self, name):
        self.edible = False
        self.name = name
class Fruit(Plant):
    def __init__(self, name):
        self.edible = True
        self.name = name

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
