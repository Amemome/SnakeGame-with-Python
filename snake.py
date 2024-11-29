import object,pygame
from collections import deque

class Snake(object.GameObject):
    """플레이어가 조작할 수 있는 뱀 클래스"""

    def __init__(self, x=0, y=0,color=(255,0,0)):
        super().__init__(x, y, color)
        self.head = [x,y] # 초기 머리 위치
        self.body = deque([(x,y)]) # 몸통은 덱으로 관리.
        self.speed = [0,0]
        self.length = 1     # 현재 길이
        self.isDead = False
        self.cellSize = 20
    
    def setDirection(self,dir):
        if(dir == "right"):
            self.speed = [self.cellSize,0]
        if(dir == "left"):
            self.speed = [-self.cellSize,0]
        if(dir == "up"):
            self.speed = [0,-self.cellSize]           
        if(dir == "down"):
            self.speed = [0,self.cellSize]

    def addLength(self,n):
        self.length += n

    def move(self):
        self.head[0] += self.speed[0]
        self.head[1] += self.speed[1]
        self.body.append(list(tuple(self.head)))

        if(self.length == len(self.body)-1):
            self.body.popleft()
        

    def checkEatFood(self,food):
        foodPos = food.getPosition()
        return tuple(self.head) == foodPos


    def checkCollision(self,X,Y):
        # 화면 밖으로 나가면 아웃.
        if (self.head[0] < 0 or self.head[0] >= X): self.isDead = True
        if (self.head[1] < 0 or self.head[1] >= Y): self.isDead = True
        if list(self.head) in list(self.body)[:-1]: self.isDead = True # 몸통 Deque 에 머리가 속하면 충돌됨.
        print(f"head : {self.head} \n body : {self.body}")

        return self.isDead

        
    def draw(self,screen):
        for bd in self.body:
            pygame.draw.rect(screen,self.color,(bd[0], bd[1], self.cellSize, self.cellSize))
