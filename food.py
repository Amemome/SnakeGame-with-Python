import random,object

class Food(object.GameObject):
    def __init__(self, x, y, color):
        super().__init(x,y,color)

    # def setRandom(self):
    #     self.x = random.randint(0,)

    def IsEaten(self, snake):
        pass #뱀에게 먹혔을 때의 코드, 추가 바람

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
