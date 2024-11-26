import random

class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def ItemRandomPosition(self, width, height):
        self.x = random.randint(0, width - 1)
        self.y = random.randint(0, height - 1)

    def IsEaten(self, snake):
        pass

class Item1(Food):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = 'Item1'
        self.points = 100

class Item2(Food):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = 'Item2'
        self.points = 200

class Item3(Food):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = 'Item3'
        self.points = 300