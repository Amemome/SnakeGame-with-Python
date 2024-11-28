import pygame

class GameObject:
    """모든 게임 요소가 가지는 속성으로서 위치(좌표) , 색깔을 가진다."""
    cellSize = 0
    
    def __init__(self,x,y,color = (0,0,0)):
        self.x = x
        self.y = y
        self.color = color
    
    def setColor(self,color):
        self.color = color
    
    def setPosition(self,x,y):
        self.x = x
        self.y = y
    
    def draw(self, screen):
        pygame.draw.rect(screen)