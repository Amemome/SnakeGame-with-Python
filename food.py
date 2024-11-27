import random,obj

class Food(obj.GameObject):
    def __init__(self, x, y, color):
        super().__init(x,y,color)

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