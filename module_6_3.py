#Домашнее задание по теме "Множественное наследование"
class Horse:
    x_distance = 0 # Пройденный путь
    sound = 'Frrr' #Звук лошади
    def run(self, dx: int):
        self.x_distance += dx
        return self.x_distance
class Eagle:
    y_distance = 0 #Высота полета
    sound = 'I train, eat, sleep, and repeat' # Звук орла
    def fly(self, dy: int):
        self.y_distance += dy
        return self.y_distance
class Pegasus(Horse, Eagle):
    def __init__(self):
        self.sound = Horse().sound
        self.sound = Eagle().sound
    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)
    def get_pos(self):
        pos_pegaus = (self.x_distance, self.y_distance)
        return pos_pegaus
    def voice(self):
        print(self.sound)

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
