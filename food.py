import random,object

class Food(object.GameObject):
    def __init__(self,  x, y,color):
        super().__init__(x,y,color)
        self.point = 0

    def setPosition(self,width,height,cellsize): # 다형성 사용. 메서드 오버라이딩
        self.x = random.randint(0, width // cellsize) * cellsize
        self.y = random.randint(0, height // cellsize) * cellsize

    def getPoint(self):
        return self.point


class Item1(Food):
    def __init__(self, x=0, y=0):
        super().__init__(x, y,(235, 222, 52))
        self.type = 'Item1'
        self.point = 1


class Item2(Food):
    def __init__(self, x=0, y=0):
        super().__init__(x, y,(52, 235, 67))
        self.type = 'Item2'
        self.point = 2

class Item3(Food):
    def __init__(self, x=0, y=0):
        super().__init__(x, y,(52, 61, 235))
        self.type = 'Item3'
        self.point = 3