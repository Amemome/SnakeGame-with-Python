import object,pygame
from collections import deque

class Snake(object.GameObject):
    """플레이어가 조작할 수 있는 뱀 클래스"""

    def __init__(self, x=0, y=0,color=(255,0,0)):
        super().__init__(x, y, color)
        self.head = [x,y] # 중간 지점에 머리를 둠.
        self.body = deque([(x,y)]) # 몸통은 덱으로 관리.
        self.speed = [0,0]
        self.length = 1    
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
        self.body.popleft()
        # if(self.length > len(self.body)-1):
            

        self.length = len(self.body) # 길이를 업데이트 해줍니다.

    def checkCollision(self,X,Y):
        # 화면 밖으로 나가면 아웃.
        if(self.head[0] < 0 or self.head[0] >= X): self.isDead = True
        if(self.head[1] < 0 or self.head[1] >= Y): self.isDead = True
        if(tuple(self.head) in self.body): self.isDead = True # 몸통 Deque 에 머리가 속하면 충돌됨.
        return self.isDead

        
    def draw(self,screen):
        for bd in self.body:
            pygame.draw.rect(screen,self.color,(bd[0], bd[1], self.cellSize, self.cellSize))
