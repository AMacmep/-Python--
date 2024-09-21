# Домашнее задание по теме "Множественное наследование"
class Horse:
    def __init__(self):
        self.x_distance = 0  # Пройденный путь
        self.sound = 'Frrr'  # Звук лошади

    def run(self, dx: int):
        self.x_distance += dx
        return self.x_distance


class Eagle:
    def __init__(self):
        self.y_distance = 0  # Высота полета
        self.sound = 'I train, eat, sleep, and repeat'  # Звук орла

    def fly(self, dy: int):
        self.y_distance += dy
        return self.y_distance


class Pegasus(Horse, Eagle):
    def __init__(self):
        super().__init__()
        Horse.__init__(self)
        Eagle.__init__(self)

    # Eagle.__init__(self, sound)

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
