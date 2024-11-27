import obj,queue,pygame

class Snake(obj.GameObject):
    """플레이어가 조작할 수 있는 뱀 클래스"""

    def __init__(self, x=24, y=18,color=(255,0,0)):
        super().__init__(x, y, color)
        self.head = [x,y] # 중간 지점에 머리를 둠.
        self.body = queue() # 몸통은 덱으로 관리.
        self.speed = [0,0]
    
    def setDirection(self,dir):
        if(dir == "up"):
            self.speed = [20,0]
        if(dir == "down"):
            self.speed = [-20,0]
        if(dir == "left"):
            self.speed = [0,-20]           
        if(dir == "right"):
            self.speed = [0,20]

    def update(self):
        self.head[0] += self.speed[0]
        self.head[1] += self.speed[1]
        
    def draw(self,screen):
        pygame.draw.rect(screen,self.color,(self.head[0], self.head[1], self.cellSize, self.cellSize))